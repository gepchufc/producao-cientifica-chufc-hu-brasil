"""Painel público. Executa somente sobre indicadores previamente agregados."""
from __future__ import annotations
import json
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from indicadores import UNIDADES, filtrar_serie, matriz_instituicoes, crescimento_anual
from tema_chufc import aplicar_tema, cabecalho, layout_fig, VERDE, AZUL, AMBAR

BASE=Path(__file__).resolve().parent
ARQUIVO=BASE/'data'/'indicadores_agregados.json'
st.set_page_config(page_title='Produção Científica CH-UFC / HU Brasil',page_icon='📈',layout='wide')
aplicar_tema()

@st.cache_data
# Arquivo agregado é o único dado acessado pelo dashboard público.
def ler_indicadores(caminho:str, modificado:float)->dict:
    with open(caminho,encoding='utf-8') as f:
        return json.load(f)

if not ARQUIVO.is_file():
    st.error('Arquivo de indicadores não localizado. Verifique data/indicadores_agregados.json.')
    st.stop()

info=ler_indicadores(str(ARQUIVO),ARQUIVO.stat().st_mtime)
anos=[int(r['ano']) for r in info['serie_anual']]
ano_min,ano_max=min(anos),max(anos)
with st.sidebar:
    st.markdown('### Painel de indicadores')
    st.caption('Dados bibliométricos agregados · Consulta pública')
    unidade=st.selectbox('Instituição',['Consolidado CH-UFC',*UNIDADES])
    intervalo=st.slider('Período de publicação',min_value=ano_min,max_value=ano_max,value=(ano_min,ano_max))
    st.divider()
    st.caption('Indicadores calculados exclusivamente a partir de publicações com afiliação hospitalar identificada.')

cabecalho('HUWC · MEAC · Panorama institucional e evolução histórica', 'PAINEL PÚBLICO · INDICADORES AGREGADOS')
coleta=info['metadados'].get('ultima_coleta_concluida_utc','')
if coleta:
    st.caption('Última execução de coleta concluída: '+coleta[:10].split('-')[2]+'/'+coleta[:10].split('-')[1]+'/'+coleta[:10].split('-')[0]+' (UTC).')

serie=filtrar_serie(info,*intervalo,unidade)
crescimento=crescimento_anual(serie,__import__('datetime').date.today().year)
ativos=serie.loc[serie['artigos'].gt(0)]
total=int(serie['artigos'].sum())
anos_ativos=int(len(ativos))
ultimo_ano=int(ativos['ano'].max()) if anos_ativos else None
ultimo_total=int(ativos.iloc[-1]['artigos']) if anos_ativos else 0
media=round(total/max(anos_ativos,1),1)

c1,c2,c3,c4=st.columns(4)
c1.metric('Artigos no período', f'{total:,}'.replace(',','.'))
c2.metric('Anos com publicações',anos_ativos)
c3.metric('Último ano com registros',ultimo_ano if ultimo_ano else '—')
c4.metric('Média por ano ativo',str(media).replace('.',','))

visao,comparacao,metodo=st.tabs(['Evolução anual','Comparativo institucional','Metodologia e privacidade'])
with visao:
    st.subheader('Produção científica ao longo do tempo')
    graf=go.Figure()
    graf.add_trace(go.Scatter(x=serie['ano'].astype(str),y=serie['artigos'],mode='lines+markers',
        name='Artigos distintos',line=dict(color=VERDE,width=3),marker=dict(size=7,color=VERDE),
        fill='tozeroy',fillcolor='rgba(13,148,136,0.08)',hovertemplate='Ano %{x}<br>Artigos %{y}<extra></extra>'))
    fig=layout_fig(graf,altura=370)
    fig.update_layout(showlegend=False,xaxis_title=None,yaxis_title='Artigos distintos')
    fig.update_xaxes(type='category',tickangle=-45,nticks=18)
    st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})
    st.caption('O ano em andamento ainda não está completo. Mudanças na cobertura das fontes também afetam a série.')
    table=crescimento.rename(columns={'ano':'Ano','artigos':'Artigos distintos','crescimento_pct':'Variação anual (%)'})
    tabela_exibicao = table.sort_values("Ano", ascending=False).copy()

    coluna = "Variação anual (%)"

    tabela_exibicao[coluna] = tabela_exibicao[coluna].map(
        lambda valor: f"{valor:.1f}".replace(".", ",")
        if pd.notna(valor) else "—"
    )
    
    st.dataframe(
        tabela_exibicao,
        width="stretch",
        hide_index=True
    )
    st.download_button('Exportar indicadores anuais (CSV)',table.to_csv(index=False).encode('utf-8-sig'),
       'producao_anual_chufc.csv','text/csv')
with comparacao:
    st.subheader('Distribuição por unidade')
    matriz=matriz_instituicoes(info,*intervalo)
    por_unidade={u:int(matriz[u].sum()) if not matriz.empty else 0 for u in UNIDADES}
    if unidade=='Consolidado CH-UFC':
        itens=list(UNIDADES)
    else:
        itens=[unidade]
    b=go.Figure(go.Bar(x=itens,y=[por_unidade[u] for u in itens],marker_color=[VERDE if u=='HUWC' else AMBAR if u=='MEAC' else AZUL for u in itens],
        hovertemplate='%{x}<br>%{y} artigos<extra></extra>'))
    fig=layout_fig(b,altura=305)
    fig.update_layout(showlegend=False,yaxis_title='Artigos distintos')
    st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})
    st.caption('Uma publicação pode estar associada a mais de uma unidade. As barras não são aditivas.')
    st.subheader('Ano × instituição')
    if not matriz.empty:
        fig=go.Figure()
        cores={'HUWC':VERDE,'MEAC':AMBAR,'CH-UFC':AZUL}
        for u in itens:
            fig.add_trace(go.Bar(x=matriz['ano'].astype(str),y=matriz[u],name=u,marker_color=cores[u],hovertemplate='%{x}<br>'+u+': %{y}<extra></extra>'))
        fig=layout_fig(fig,altura=360)
        fig.update_layout(barmode='group',yaxis_title='Artigos por unidade',xaxis_title=None)
        fig.update_xaxes(type='category',nticks=18,tickangle=-45)
        st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})
        tabela=matriz[['ano',*itens]].rename(columns={'ano':'Ano'})
        st.dataframe(tabela.sort_values('Ano',ascending=False),hide_index=True,use_container_width=True)
        st.download_button('Exportar comparação (CSV)',tabela.to_csv(index=False).encode('utf-8-sig'),
                           'ano_instituicao_chufc.csv','text/csv')
    else:
        st.info('Não há artigos identificados nesse recorte.')
with metodo:
    st.subheader('Como os números foram produzidos')
    st.markdown("""Os indicadores foram calculados sobre um catálogo de referências bibliográficas recuperadas em bases científicas.
    Um artigo é contado uma única vez no consolidado; uma mesma publicação pode constar em duas unidades. A identificação é feita
    pela **afiliação hospitalar declarada nas referências**, e **não prova uso de dados assistenciais** nem vínculo funcional atual.""")
    st.markdown("""**Fontes consultadas:** PubMed, OpenAlex e Europe PMC. Integrações ainda não concluídas não são apresentadas como fontes confirmadas.
    **Abrangência:** pode haver publicações não identificadas; o painel não constitui inventário exaustivo de toda a produção.
    **Privacidade:** este aplicativo não disponibiliza nomes de autores, títulos, DOI/PMID, resumos, afiliações ou registros individuais.
    Somente totais previamente agregados por ano e instituição são incluídos no arquivo público.""")
    st.caption('O provedor de hospedagem poderá tratar dados técnicos de acesso conforme seus próprios termos. Para revisões sobre os dados ou a identidade institucional do projeto, consulte o canal de contato documentado no repositório.')
    st.info('Iniciativa independente de visualização bibliométrica. Não constitui painel oficial nem representa posicionamento institucional da UFC ou da HU Brasil/Ebserh.')
