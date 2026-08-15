# Requisitos iniciais

Este documento registra requisitos de produto ainda sujeitos a refinamento. Os
itens não especificam soluções elétricas; critérios quantitativos serão
adicionados somente com referências adequadas e resultados de validação.

## Funcionais

- **RF-01 — Detecção de chamada:** detectar o sinal de ring da linha.
- **RF-02 — Controle da chamada:** atender e desligar (hangup)
  eletronicamente.
- **RF-03 — Áudio:** suportar áudio bidirecional durante uma chamada.
- **RF-04 — DTMF:** suportar os tons DTMF necessários à operação do interfone.
- **RF-05 — Aparelho em paralelo:** detectar, se tecnicamente viável, quando o
  telefone/interfone físico em paralelo estiver off-hook.
- **RF-06 — Operação sem energia:** manter o telefone/interfone físico
  utilizável quando o InterBridge estiver sem alimentação.
- **RF-07 — Conectividade:** comunicar-se com o sistema móvel por Wi-Fi.
- **RF-08 — Expansão:** permitir avaliar uma futura saída por relé para abertura
  de portão por contato separado.

## Hardware

- **RH-01:** usar conectores identificados como RJ11 LINE e RJ11 PHONE.
- **RH-02:** implementar pass-through LINE → PHONE preferencialmente passivo e
  fail-safe, condicionado à validação elétrica.
- **RH-03:** basear a seção FXO/DAA no reference design oficial selecionado; não
  definir valores, pinagens, footprints ou layout sem fonte verificável.
- **RH-04:** adotar inicialmente um módulo ESP32-C3 para controle e Wi-Fi.
- **RH-05:** manter símbolos e footprints específicos do projeto em bibliotecas
  versionadas e rastreáveis às fontes técnicas.
- **RH-06:** prever pontos de teste suficientes para validação segura dos blocos,
  a serem definidos durante o projeto do esquemático.

## Segurança

- **RS-01:** identificar as tensões, correntes, transientes e condições de falha
  aplicáveis à linha antes de dimensionar a interface.
- **RS-02:** definir isolamento e distâncias de segurança com base em normas e
  documentação técnica aplicáveis, sem pressupor valores.
- **RS-03:** incluir proteção contra surtos e eventos da linha de acordo com o
  reference design validado e os requisitos da instalação-alvo.
- **RS-04:** realizar revisão de segurança antes de conectar protótipos a uma
  linha real.
- **RS-05:** considerar desde o projeto os requisitos aplicáveis a uma futura
  homologação Anatel.
- **RS-06:** documentar limitações, riscos residuais e procedimentos seguros de
  teste.

## Fabricação

- **RM-01:** manter os fontes `.kicad_pro`, `.kicad_sch`, `.kicad_pcb` e as
  bibliotecas locais sob controle de versão.
- **RM-02:** gerar BOM, Gerbers e dados de montagem de maneira reproduzível a
  partir de uma revisão identificada do projeto.
- **RM-03:** registrar fabricante, código exato e alternativas aprovadas dos
  componentes na BOM.
- **RM-04:** executar ERC, DRC e revisão dos arquivos de fabricação antes de
  liberar uma placa.
- **RM-05:** validar disponibilidade, encapsulamento e lifecycle dos componentes
  antes da compra ou montagem.

## Ainda em investigação

- seleção definitiva entre Si3050 + Si3019, Le9641 e outras alternativas;
- disponibilidade, condições de aquisição e status de ciclo de vida dos CIs;
- compatibilidade da solução com as variações de linhas de interfone/telefone
  encontradas no Brasil;
- mecanismo e confiabilidade da detecção de off-hook do aparelho em paralelo;
- requisitos de áudio, níveis, codecs e tratamento de eco;
- requisitos detalhados de alimentação e consumo;
- topologia, classificação e interface da eventual saída por relé;
- normas técnicas, ensaios e modalidade de homologação Anatel aplicáveis;
- estratégia de testes de bancada e equipamentos necessários;
- critérios quantitativos de proteção, isolamento e layout.
