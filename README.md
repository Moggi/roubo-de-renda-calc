# Roubo de renda calculator

## Definitions

Here are the values used for this calculator and its sources.

When updating the calculator with new values, make sure to use a safe source (those at gov.br).

### [INSS] - Previdência Social

Tabela para Empregado, Empregado Doméstico e Trabalhador Avulso 2022.
| Salário de Contribuição (R$) | Alíquota |
|--|--|
| Até R$ 1.212,00 | 7,5% |
| De R$ 1.212,01 a R$ 2.427,35 | 9% |
| De R$ 2.427,36 até R$ 3.641,03 | 12% |
| De R$ 3.641,04 até R$ 7.087,22 | 14% |


### [IRRF] - Imposto de Renda

Tabela para Pessoal Física a partir de 2015
| Base de cálculo (R\$) | Alíquota (\%) | Parcela a deduzir do IRPF (R\$) |
|--|--|--|
| Até 1.903,98 | 0 | 0 |
| De 1.903,99 até 2.826,65 | 7,5 | 142,80 |
| De 2.826,66 até 3.751,05 | 15 | 354,80 |
| De 3.751,06 até 4.664,68 | 22,5 | 636,13 |
| Acima de 4.664,68 | 27,5 | 869,36 |

[INSS]: https://www.gov.br/inss/pt-br/saiba-mais/seus-direitos-e-deveres/calculo-da-guia-da-previdencia-social-gps/tabela-de-contribuicao-mensal
[IRRF]: https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/tributos/irpf-imposto-de-renda-pessoa-fisica


## Development

This project makes use of [Poetry] instead of directly interact with `pip`.

Package version, python version, dependencies and some dev configs you can find at [pyproject.toml]

[Poetry]: https://github.com/python-poetry/poetry
[pyproject.toml]: ./pyproject.toml


## Test

With pytest (defined at dev dependecies at [pyproject.toml]):
```sh
pytest --doctest-modules .
```
