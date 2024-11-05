# Modelos de Conversão de Voz Adaptados - TCC II
Esse repositório possui links para as bibliotecas originais e os códigos usados para a geração das métricas usadas no meu TCC, além de algumas das especificações utilizadas, diferentes das especificações dos códigos originais.

Observe que múltiplas versões CUDA podem estar instaladas na mesma máquina, mas é necessário alterar as variáveis de ambiente do sistema para referenciar a versão a ser utilizada.

## Distorção Mel-Cepstral (MCD) e Pontuação BERT de discurso (SpeechBERTScore)
Biblioteca disponível em: https://github.com/Takaaki-Saeki/DiscreteSpeechMetrics (Último acesso em 05/11/2024)

**Ambiente:** Windows 10 pro (SO), PyCharm (IDE). Python 3.11, CUDA 12.2 (GPU GeForce GTX 1060 6gb). Numpy precisou ser rebaixado para a versão 1.24.3 (diferente da versão instalada automaticamente ao usar os comandos disponibilizados no git da biblioteca) para funcionar.

**Códigos:** mcd_test.py para a Distorção Mel-Cepstral e SBScore.py para a Pontuação BERT de discurso.

## Pseudo-Pontuação de Opinião Média (pMOS)
Biblioteca disponível em: https://github.com/lochenchou/MOSNet (Último acesso em 05/11/2024)

**Ambiente:** Windows 10 pro (SO), PyCharm (IDE). Python 3.11, CUDA 10.1 ou 10.0 (GPU GeForce GTX 1060 6gb). Versão do numpy: 1.19.5. Versão da librosa: 0.8.1. Versão do tensorflow: 2.0.0.

**Códigos:** Foi usado o código custom_test.py, já disponibilizado na biblioteca, sem alterações.

## Faixas de áudio avaliadas

As faixas de áudio avaliadas estão separadas por paridade na pasta evaluation.
