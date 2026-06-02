# =============================================================================
# Miniprojeto Avaliativo — Análise Exploratória de Dados: Base Varejo Kaggle
# Disciplina: Visualização de Dados e Business Intelligence
# Curso: CARREIRA TECH SCTEC - SENAI/SC - Lab 365 (Módulo: M1S07)
# Professor: Rodrigo Garcia Brunini
# Aluna: Natali Caroline de Miranda Stoquera
# Turma: VDBIT1
# Data de Entrega: 01/06/2026
# =============================================================================
#
# ESTRUTURA DO SCRIPT:
#   1. Importações
#   2. Constantes e Dicionário de Dados
#   3. Carregamento dos dados        (Sprint 1)
#   4. Verificação inicial (EDA)     (etapa exploratória — boa prática)
#   5. Transformação de tipos        (Sprint 2)
#   6. Limpeza de nulos e duplicatas (Sprint 3)
#   7. Estatísticas descritivas      (Sprint 4)
#   8. Agrupamentos                  (Sprint 5)
#   9. Relatório e exportação        (Sprint 6)
#  10. Pipeline principal            (main)
#
# NOTA DE DESENVOLVIMENTO — REUSO DO MINIPROJETO DJANGO LIVRE:
# Estrutura de funções separadas, constantes centralizadas, padrão de
# impressão com separadores "=" e exportação com utf-8-sig reaproveitados
# do script limpeza_DjangoLivre.py (Grupo Django Livre, maio/2026).
# As funções foram reescritas para a Base Varejo, pois cada base tem
# suas próprias colunas e regras de negócio.
#
# =============================================================================
# DICIONÁRIO DE DADOS
# Fonte: INFORMAÇÕES_LEIA-ME.md — Prof. Rodrigo Garcia Brunini
#
# 1. DATA: Data da compra
# 2. CO_ID: Identificação do número de compra (número da nota fiscal)
# 3. CL_ID: Identificação do cliente (número do cliente)
# 4. CL_GENERO: Sexo biológico informado pelo cliente
# 5. CL_EC: Estado civil do cliente
#      - 1 = Casado ou união estável
#      - 2 = Divorciado
#      - 3 = Separado
#      - 4 = Solteiro
#      - 5 = Viúvo
# 6. CL_FHL: Número de filhos do cliente
# 7. CL_SEG: Segmentação econômica do cliente (classe A, B ou C)
# 8. PR_ID: Código do produto (SKU) adquirido
# 9. PR_CAT: Categoria do produto adquirido
# 10.PR_NOME: Nome do produto adquirido
# =============================================================================


# 1. IMPORTAÇÕES
# Carregamento das bibliotecas que serão utilizadas.
# pandas → manipulação de tabelas (DataFrames)
# datetime → para obter a data de hoje e validar datas
# =============================================================================

import pandas as pd                 # biblioteca principal para análise de dados
from datetime import date           # usada na seção 5 para checar datas futuras
import os                           # para montar caminhos de arquivo compatíveis


# =============================================================================
# 2. CONSTANTES
# Caminhos centralizados aqui — se o arquivo mudar de local, alteramos só aqui.
# os.path.dirname(__file__) → pasta onde este script está salvo
# os.path.join()            → monta o caminho de forma segura (Windows/Linux/Mac)
# Padrão reaproveitado do Django Livre (seção 2).
# =============================================================================

CAMINHO_ENTRADA = os.path.join(os.path.dirname(__file__), "Base Varejo.csv")
CAMINHO_SAIDA   = os.path.join(os.path.dirname(__file__), "df_limpo_NataliStoquera_VDBIT1.csv")


# =============================================================================
# 3. CARREGAMENTO DOS DADOS (Sprint 1)
# Carrega o arquivo CSV com pandas e exibe informações básicas da base
# Estrutura de função reaproveitada do Django Livre (seção 3).
# =============================================================================

def carregar_dados(caminho: str) -> pd.DataFrame:
    """Carrega o CSV e exibe as informações básicas da base."""

    print("=" * 65)
    print("SPRINT 1 — CARREGAMENTO DOS DADOS")
    print("=" * 65)

    # read_csv lê o arquivo e cria a tabela (DataFrame) na memória
    df = pd.read_csv(caminho, sep=";")

    print(f"\n Registros carregados:\n{len(df):,}")
    print(f"\n Colunas encontradas:\n{len(df.columns)}")
    print(f"\n Colunas e tipos de dados:\n{df.dtypes}")
    print(f"\n Amostra (3 primeiras linhas):\n{df.head(3)}")

    return df      # devolve o DataFrame para a próxima etapa


# =============================================================================
# 4. VERIFICAÇÃO INICIAL - EDA
# Identifica e reporta problemas antes de qualquer alteração.
# Boas práticas: sempre olhar a base crua primeiro, antes de mexer nela.
# Esta função NÃO altera o DataFrame — retorno None.
# Padrão de impressão reaproveitado do Django Livre (seções 4 e 5).
# =============================================================================

def verificar_qualidade(df: pd.DataFrame) -> None:

    print("\n" + "=" * 65)
    print("EDA — VERIFICAÇÃO INICIAL DA BASE")
    print("=" * 65)

    # df.shape → tupla (linhas, colunas)
    print(f"\n Dimensões: {df.shape[0]:,} linhas x {df.shape[1]} colunas")

    # isnull().sum() → conta células vazias por coluna
    print(f"\n Nulos por coluna:\n{df.isnull().sum().to_string()}")

    # duplicated().sum() → conta linhas completamente idênticas
    print(f"\n Registros duplicados: {df.duplicated().sum():,}")

    # Categorias inválidas — "#N/D" é erro do Excel para "não disponível"
    print(f"\n Categorias '#N/D' em PR_CAT: {(df['PR_CAT'] == '#N/D').sum():,}")

    # Colunas Unnamed → geradas pelo Excel ao salvar com colunas extras em branco
    colunas_fantasma = [c for c in df.columns if c.startswith("Unnamed")]
    print(f"\n Colunas desnecessárias (Unnamed): {colunas_fantasma}")


# =============================================================================
# 5. TRANSFORMAÇÃO DE TIPOS (Sprint 2)
# Converte colunas para os tipos corretos conforme o dicionário de dados.
# Feito antes da limpeza para garantir tipos corretos durante a remoção.
# Padrão to_datetime reaproveitado do Django Livre (seção 11).
# =============================================================================

def transformar_tipos(df: pd.DataFrame) -> pd.DataFrame:

    print("\n" + "=" * 65)
    print("SPRINT 2 — TRANSFORMAÇÃO DE TIPOS")
    print("=" * 65)

    # ── DATA: string → datetime ───────────────────────────────────
    # format="%d/%m/%Y" → formato exato da string na base ("01/02/2019")
    # errors="coerce" → datas impossíveis viram NaT em vez de erro
    df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
    print(f"\n [A] DATA convertida para datetime. Exemplo: {df['DATA'].iloc[0]}")

    # ── Colunas de texto: garantir string sem espaços extras ──────
    # .astype(str) → converte para texto
    # .str.strip() → remove espaços no início e no fim
    # Evita por exemplo que "  ALIMENTOS" e "ALIMENTOS" sejam categorias diferentes
    for col in ["CL_GENERO", "CL_SEG", "PR_CAT", "PR_NOME"]:
        df[col] = df[col].astype(str).str.strip()
    print(f"\n [B] Colunas de texto padronizadas: CL_GENERO, CL_SEG, PR_CAT, PR_NOME")

    # ── Colunas numéricas: garantir tipo numérico ─────────────────
    # errors="coerce" → valores não numéricos viram NaN em vez de erro
    for col in ["CO_ID", "CL_ID", "CL_EC", "CL_FHL", "PR_ID"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    print(f"\n [C] Colunas numéricas convertidas: CO_ID, CL_ID, CL_EC, CL_FHL, PR_ID")

    # ── Validação do CO_ID ────────────────────────────────────────
    # Conforme observado na amostra do dicionário de dados,
    # os identificadores de compra começam a partir de 1000.
    co_invalidos = (df["CO_ID"] < 1000).sum()
    print(f"\n [D] CO_ID menores que 1000 (inválidos): {co_invalidos}")

    return df.reset_index(drop=True)


# =============================================================================
# 6. LIMPEZA DE NULOS E DUPLICATAS (Sprint 3)
# Identifica e trata valores ausentes e registros duplicados.
# Separado do Sprint 2 — primeiro corrigimos tipos, depois limpamos.
# Padrão de remoção reaproveitado do Django Livre (seções 6 e 9).
# =============================================================================

def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:

    print("\n" + "=" * 65)
    print("SPRINT 3 — LIMPEZA DE NULOS E DUPLICATAS")
    print("=" * 65)

    # ── Remover colunas Unnamed ───────────────────────────────────
    # 100% nulas — removê-las evita colunas em branco em análises
    colunas_validas = [c for c in df.columns if not c.startswith("Unnamed")]
    df = df[colunas_validas].copy()  # .copy() evita alertas do pandas
    print(f"\n [A] Colunas válidas mantidas: {list(df.columns)}")

    # ── Remover duplicatas ────────────────────────────────────────
    # keep="first" → mantém a primeira ocorrência, remove as demais
    antes = len(df)
    df = df.drop_duplicates(keep="first")
    print(f"\n [B] Duplicatas removidas: {antes - len(df):,}")
    print(f"Registros restantes: {len(df):,}")

    # ── Tratar PR_CAT inválida com lógica if/else ─────────────────
    # "#N/D" é o código de erro do Excel para "não disponível".
    # Substituímos por "Sem Categoria" em vez de remover o registro:
    # o produto e a compra existem — só a categoria está ausente.
    # Remover descartaria dados de venda reais.
    # Padrão replace reaproveitado do Django Livre (seção 9).
    qtd_nd = (df["PR_CAT"] == "#N/D").sum()

    if qtd_nd > 0:
        df["PR_CAT"] = df["PR_CAT"].replace("#N/D", "Sem Categoria")
        print(f"\n [C] Categorias '#N/D' → 'Sem Categoria': {qtd_nd:,} registros")
    else:
        print("\n [C] Nenhuma categoria inválida encontrada")
    
    # ── Verificar nulos restantes ─────────────────────────────────
    print(f"\n [D] Nulos restantes por coluna:\n{df.isnull().sum().to_string()}")

    print(f"\n Base limpa: {len(df):,} registros | {len(df.columns)} colunas")

    return df.reset_index(drop=True)  # reorganiza os índices após remoções


# =============================================================================
# 7. ESTATÍSTICAS DESCRITIVAS (Sprint 4)
# Parâmetros da coluna CL_FHL (número de filhos dos clientes).
# =============================================================================

def estatisticas_filhos(df: pd.DataFrame) -> None:
    # Retorno None — só imprime, não altera o DataFrame

    print("\n" + "=" * 65)
    print("SPRINT 4 — ESTATÍSTICAS DESCRITIVAS: CL_FHL (Nº de Filhos)")
    print("=" * 65)

    filhos = df["CL_FHL"]  # atalho para não repetir df["CL_FHL"] em cada linha

    # .mean()   → média aritmética (soma ÷ quantidade)
    # .median() → valor do meio quando os dados estão ordenados
    # .std()    → desvio padrão — dispersão em torno da média
    # .mode()   → valor mais frequente ([0] pega o primeiro caso haja empate)
    # .max()    → maior valor | .min() → menor valor
    # .count()  → registros não nulos
    print(f"\nMédia: {filhos.mean():.2f}")
    print(f"\nMediana: {filhos.median():.1f}")
    print(f"\nDesvio Padrão: {filhos.std():.2f}")
    print(f"\nModa: {int(filhos.mode()[0])}")
    print(f"\nMáximo: {int(filhos.max())}")
    print(f"\nMínimo: {int(filhos.min())}")
    print(f"\nContagem: {filhos.count():,}")


# =============================================================================
# 8. AGRUPAMENTOS (Sprint 5)
# Explora padrões com groupby() e pivot_table().
# groupby() → agrupa linhas por uma coluna e conta registros
# pivot_table() → tabela cruzada entre duas variáveis
# =============================================================================

def explorar_agrupamentos(df: pd.DataFrame) -> None:
    # Retorno None — só imprime, não altera o DataFrame

    print("\n" + "=" * 65)
    print("SPRINT 5 — PADRÕES DE AGRUPAMENTO")
    print("=" * 65)

    # ── Agrupamento 1: itens por gênero ───────────────────────────
    # .size() → conta linhas por grupo | .sort_values() → ordena maior→menor
    print("\n [1] Itens comprados por Gênero:")
    print(df.groupby("CL_GENERO").size().sort_values(ascending=False))

    # ── Agrupamento 2: itens por categoria ────────────────────────
    print("\n [2] Itens vendidos por Categoria:")
    print(df.groupby("PR_CAT").size().sort_values(ascending=False))

    # ── Agrupamento 3: pivot segmento × gênero ────────────────────
    # pivot_table cruza duas variáveis em uma tabela de dupla entrada:
    # linhas = CL_SEG (segmento econômico) | colunas = CL_GENERO
    # aggfunc="size" conta quantos itens existem em cada combinação
    # fill_value=0 → células sem registros recebem zero em vez de vazio
    print("\n  [3] Itens por Segmento Econômico × Gênero (pivot):")
    tabela = pd.pivot_table(
        df,
        index="CL_SEG",      # segmento nas linhas (A, B, C)
        columns="CL_GENERO", # gênero nas colunas (F, M)
        aggfunc="size",      # função: contar registros
        fill_value=0         # zero onde não há registros
    )
    print(tabela)


# =============================================================================
# 9. RELATÓRIO FINAL E EXPORTAÇÃO (Sprint 6)
# Gera um resumo da base limpa e exporta o arquivo final.
# =============================================================================

def relatorio_e_exportar(df, caminho_saida):

    print("\n--- RELATÓRIO FINAL ---")

    # Indicadores principais
    total_registros = len(df)
    total_notas = df["CO_ID"].nunique()
    total_clientes = df["CL_ID"].nunique()
    total_produtos = df["PR_NOME"].nunique()
    total_nulos = df.isnull().sum().sum()

    # Insights de negócio
    categoria_lider = df["PR_CAT"].value_counts().idxmax()
    genero_lider = df["CL_GENERO"].value_counts().idxmax()

    print(f"""
RESUMO TÉCNICO
- Registros: {total_registros:,}
- Notas fiscais: {total_notas:,}
- Clientes únicos: {total_clientes:,}
- Produtos distintos: {total_produtos:,}
- Nulos restantes: {total_nulos}

INSIGHTS DE NEGÓCIO

1. Categoria líder:
   A categoria '{categoria_lider}' apresentou a maior quantidade de vendas.
   Esse resultado sugere uma demanda maior por esses produtos e pode ajudar
   no planejamento de estoque e promoções.

2. Perfil de compras:
   O gênero '{genero_lider}' foi o que mais realizou compras na base analisada.
   Essa informação pode auxiliar em futuras ações de marketing direcionadas.

3. Filhos dos clientes:
   A moda e a mediana da quantidade de filhos foram iguais a 0,
   indicando que a maior parte dos clientes não possui filhos.
   Entretanto, a média superior a 1 sugere a existência de grupos
   familiares que realizam compras em maior volume.

4. Segmento econômico:
   A Classe B concentrou a maior parte das vendas registradas,
   seguida pelas Classes C e A.
   Isso indica que o público predominante da empresa pertence à Classe B.

5. Qualidade dos dados:
   Foram removidos registros duplicados e tratados valores ausentes,
   contribuindo para uma base mais consistente e confiável para análise.

6. Limitação da análise:
   Como a base não possui informações de preço ou faturamento,
   não foi possível calcular indicadores financeiros, como receita
   total ou ticket médio das compras.
""")

    df.to_csv(caminho_saida, index=False, encoding="utf-8-sig")

    print(f"Arquivo salvo em: {caminho_saida}")

# =============================================================================
# 10. PIPELINE PRINCIPAL
# O main() chama cada função na ordem correta — não faz nada sozinho.
# "if __name__ == '__main__'" garante que o pipeline só roda ao executar
# este arquivo diretamente. Se outro script importar nossas funções,
# o pipeline NÃO dispara automaticamente.
# Padrão reaproveitado do Django Livre (seção 15).
# =============================================================================

def main() -> None:

    print("=" * 65)
    print("  MINI-PROJETO AED — BASE VAREJO | SENAI/SC Lab 365 — M1S07")
    print("=" * 65)

    df = carregar_dados(CAMINHO_ENTRADA)    # Sprint 1 — carrega o CSV
    verificar_qualidade(df)                 # EDA — diagnóstico sem alterar
    df = transformar_tipos(df)              # Sprint 2 — converte tipos
    df = limpar_dados(df)                   # Sprint 3 — remove nulos e duplicatas
    estatisticas_filhos(df)                 # Sprint 4 — estatísticas de CL_FHL
    explorar_agrupamentos(df)               # Sprint 5 — agrupamentos
    relatorio_e_exportar(df, CAMINHO_SAIDA) # Sprint 6 — relatório e exportação

    print("\n" + "=" * 65)
    print("PIPELINE CONCLUÍDO COM SUCESSO!")
    print("=" * 65)

# Gatilho de execução — dispara o main() ao rodar o arquivo
if __name__ == "__main__":
    main()
