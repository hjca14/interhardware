#!/usr/bin/env python3
"""Read-only KiCad PCB inventory and schematic/PCB reference parity audit."""
import csv, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def blocks(text, token):
    pos=0
    while (start:=text.find(token,pos)) >= 0:
        depth=0; quoted=False; escaped=False
        for end in range(start,len(text)):
            char=text[end]
            if quoted:
                if escaped: escaped=False
                elif char=='\\': escaped=True
                elif char=='"': quoted=False
            elif char=='"': quoted=True
            elif char=='(': depth+=1
            elif char==')':
                depth-=1
                if depth==0:
                    yield text[start:end+1]; pos=end+1; break
        else: raise ValueError(f'unclosed block at {start}')

def prop(block,name):
    match=re.search(r'\(property "'+re.escape(name)+r'" "((?:\\.|[^"\\])*)"',block)
    return match.group(1) if match else ''

def pcb_parts():
    text=(ROOT/'kicad/interhardware.kicad_pcb').read_text()
    for block in blocks(text,'\t(footprint '):
        ref=prop(block,'Reference')
        if not ref: continue
        footprint=re.match(r'\s*\(footprint "([^"]+)"',block).group(1)
        layer=re.search(r'\n\s*\(layer "([^"]+)"\)',block).group(1)
        pads=[]
        for pad in blocks(block,'\t\t(pad '):
            match=re.match(r'\s*\(pad "([^"]*)" ([^ ]+)',pad)
            if match and match.group(2)!='np_thru_hole': pads.append(match.group(1))
        yield dict(Ref=ref,Value=prop(block,'Value'),Manufacturer=prop(block,'Manufacturer'),
                   MPN=prop(block,'MPN'),Description=prop(block,'Description'),Package=prop(block,'Package'),
                   Footprint=footprint,DNP='No',Side='Top' if layer=='F.Cu' else 'Bottom',
                   Status='PLACED',Electrical_Pads=str(len(set(pads))))

def schematic_refs():
    text=(ROOT/'kicad/interhardware.kicad_sch').read_text()
    refs=[]
    # Placed symbols have an instances block; library definitions do not.
    for block in blocks(text,'\t(symbol\n'):
        if '(instances' not in block: continue
        ref=prop(block,'Reference')
        if ref and not ref.startswith('#'): refs.append(ref)
    return refs

def main():
    parts=sorted(pcb_parts(),key=lambda p:(re.sub(r'\d.*','',p['Ref']),int(re.search(r'\d+',p['Ref']).group()) if re.search(r'\d+',p['Ref']) else 0,p['Ref']))
    refs=[p['Ref'] for p in parts]; sch=schematic_refs()
    errors=[]
    for label, values in [('PCB',refs),('schematic',sch)]:
        dup=sorted({x for x in values if values.count(x)>1})
        if dup: errors.append(f'{label} duplicate references: {dup}')
    if set(refs)!=set(sch): errors.append(f'parity mismatch: schematic-only={sorted(set(sch)-set(refs))}; PCB-only={sorted(set(refs)-set(sch))}')
    if any(not p['Footprint'] for p in parts): errors.append('missing footprint')
    if any(p['Side']!='Top' for p in parts): errors.append('non-top-side component')
    out=ROOT/'manufacturing/reports/COMPONENT_INVENTORY.csv'; out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=parts[0].keys()); writer.writeheader(); writer.writerows(parts)
    print(f'{len(parts)} PCB components; {len(sch)} schematic components; wrote {out.relative_to(ROOT)}')
    if errors:
        print('\n'.join(errors),file=sys.stderr); return 1
    print('PASS: unique 1:1 schematic/PCB references, footprints present, all components top-side')
    return 0
if __name__=='__main__': raise SystemExit(main())
