# Pandemic: Hollow Knight Edition

Este projeto é uma implementação digital do jogo de tabuleiro *Pandemic*, adaptado para o universo do jogo *Hollow Knight*. O desenvolvimento busca aplicar práticas de Gerência de Projeto e Manutenção de Software, como controle de versão, uso de issues e integração contínua, em um ambiente colaborativo e prático.

## Objetivo do Jogo

Desenvolver um jogo **cooperativo digital**, inspirado no *Pandemic: Hot Zone – Europa*, no qual **três jogadores** devem conter e curar **três doenças fictícias** — Infecção, Esporos Fúngicos e Vazio — que se espalham por 18 regiões do universo de Hollow Knight.

## Regras Principais

- **Jogadores:** 3 especialistas com habilidades únicas
- **Doenças:** Infecção (laranja), Esporos Fúngicos (verde), Vazio (roxo)
- **Cidades:** 18 localizações icônicas do universo Hollow Knight
- **Cartas:**
  - 24 de cidade (18 cidades únicas + 6 duplicadas)
  - 24 de infecção
  - 4 de evento
  - 3 de epidemia
- **Cubos de doença:** 16 por cor (48 no total)
- **Turnos:** Cada jogador realiza 4 ações por rodada
- **Ações possíveis:** mover, tratar doença, compartilhar carta, descobrir cura, usar evento
- **Fim de turno:** comprar 2 cartas de jogador e infectar cidades (2 a 4 cartas)
- **Epidemias:** aumentam nível de infecção, causam surtos e reciclam descarte
- **Surtos:** 4º cubo → espalha para cidades conectadas; 5 surtos = derrota

## Especialistas Jogáveis

| Especialista               | Personagem |    Habilidade                                                             |
|----------------------------|------------|---------------------------------------------------------------------------|
| Especialista em Quarentena | Cavaleiro  | Impede infecção na sua cidade e nas cidades conectadas                    |
| Médica                     | Hornet     | Remove todos os cubos de uma doença com apenas 1 ação                     |
| Analista de Campo          | Cornifer   | Pode dar qualquer carta para outro jogador, independentemente da cidade   |
| Coordenador de Campo       | Grimm      | Move outro jogador como se fosse ele, gastando cartas                     | 
| Cientista                  | Monomon    | Descobre cura com apenas 3 cartas da mesma doença                         |

## Cidades do Jogo

**Infecção (laranja):**  
Penhascos Uivantes, Dirtmouth, Pico de Cristal, Encruzilhada Esquecida, Cidade das Lágrimas, Terra do Descanso

**Esporos Fúngicos (verde):**  
Caminho Verde, Jardins da Rainha, Cânion da Névoa, Ermos Fúngicos, Hidrovia Real, Vila dos Louva-a-Deus

**Vazio (roxo):**  
Ninho Profundo, Bacia Antiga, Borda do Reino, A Colmeia, Coliseu dos Tolos, Abismo

## Condições de Vitória e Derrota

- **Vitória:** Curar todas as 3 doenças
- **Derrota:** Ocorre se qualquer uma das seguintes condições for atingida:
  - 5 surtos
  - Fim do baralho de jogador
  - Esgotamento dos cubos de uma das doenças

## Equipe
- Isadora Duarte
- Izabel Soares
- Lylian Pacheco
- Nayara Dornelas
- Guilherme Vieira
- Mateus Sacramento