"""Agregações e filtros para indicadores públicos sem microdados."""
from __future__ import annotations
import pandas as pd

UNIDADES = ("HUWC", "MEAC", "CH-UFC")


def filtrar_serie(dados: dict, ano_inicio: int, ano_fim: int, unidade: str) -> pd.DataFrame:
    if unidade == "Consolidado CH-UFC":
        base = pd.DataFrame(dados["serie_anual"])
    elif unidade in UNIDADES:
        base = pd.DataFrame(dados["ano_instituicao"])
        base = base.loc[base["unidade"] == unidade, ["ano", "artigos"]]
    else:
        raise ValueError("Unidade inválida")
    periodo = pd.DataFrame({"ano": list(range(ano_inicio, ano_fim + 1))})
    resultado = periodo.merge(base, on="ano", how="left")
    resultado["artigos"] = resultado["artigos"].fillna(0).astype(int)
    return resultado


def matriz_instituicoes(dados:dict, ano_inicio:int, ano_fim:int) -> pd.DataFrame:
    base=pd.DataFrame(dados["ano_instituicao"])
    base=base[base["ano"].between(ano_inicio, ano_fim)]
    if base.empty:
        return pd.DataFrame(columns=["ano",*UNIDADES])
    tabela=(base.pivot_table(index="ano",columns="unidade",values="artigos",aggfunc="sum",fill_value=0)
              .reindex(columns=UNIDADES,fill_value=0).reset_index())
    return tabela


def crescimento_anual(serie:pd.DataFrame, ano_corrente:int) -> pd.DataFrame:
    r=serie.copy().sort_values("ano")
    anterior=r["artigos"].shift(1)
    r["crescimento_pct"]=(100*(r["artigos"]-anterior)/anterior.where(anterior.ne(0))).round(1)
    r.loc[r["ano"] >= ano_corrente,"crescimento_pct"]=float("nan")
    return r
