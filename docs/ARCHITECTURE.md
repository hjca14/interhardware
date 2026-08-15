# Arquitetura do sistema

## Visão de alto nível

```text
LINE RJ11
  |
  +------------------------------------------> PHONE RJ11
  |
  +--> proteção / DAA --> Si3019 <isolamento> Si3050 --> ESP32-C3
                                                        |
                                                        +--> Wi-Fi
                                                        |
                                                        +--> saída por relé (opcional/futura)
```

O diagrama representa apenas os blocos funcionais; ele **não é um circuito** e
não define pinagens, valores, footprints, componentes de proteção nem a solução
de isolamento. Esses detalhes só serão incorporados ao esquemático a partir da
documentação oficial aplicável e depois de revisão técnica.

## Caminho telefônico

O conector LINE recebe a linha analógica. Um ramo segue para a interface
telefônica FXO/DAA planejada em torno do Si3019 (lado da linha) e do Si3050 (lado
do sistema). A implementação desse ramo deverá partir do reference design
oficial da Skyworks, preservando os requisitos de isolamento, proteção, BOM e
layout que forem confirmados durante a pesquisa.

O segundo ramo conecta LINE a PHONE para que o telefone/interfone existente
permaneça disponível. O pass-through deve ser idealmente **passivo e fail-safe**:
a ausência de alimentação ou uma falha do InterBridge não deve, por si só,
interromper o uso do aparelho físico. A topologia exata e seu efeito sobre a
linha ainda precisam de validação em bancada e de uma análise de segurança.

## Controle e conectividade

O módulo ESP32-C3 será responsável pelo controle da interface telefônica e pela
comunicação via Wi-Fi com o restante do sistema. Interfaces digitais, sinais de
áudio, alimentação e firmware ainda serão definidos após a seleção definitiva
dos componentes e a validação da documentação oficial.

Uma saída por relé é uma extensão futura para instalações que disponibilizem um
contato separado de abertura de portão. Ela não faz parte do primeiro circuito
e deverá ter requisitos elétricos e de segurança próprios antes da inclusão.
