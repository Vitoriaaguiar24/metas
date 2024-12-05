import streamlit as st

st.title('Suas Metas!')

st.subheader("Escreva as suas metas do dia e marque-as quando você realizá-las.")

# Verificando se a lista de metas já existe no estado da sessão
if 'lista_itens' not in st.session_state:
    st.session_state.lista_itens = []

# Função para marcar itens de uma lista
def marcar_itens(lista):
    itens_selecionados = []
    for i, item in enumerate(lista):  # Usando enumerate para obter índice e item
        if st.checkbox(f'{item}', key=f"opcao_{i}"):  # Cada item recebe um checkbox com chave única
            itens_selecionados.append(item)
            
    return itens_selecionados

# Interface para adicionar novas metas
with st.form(key='form_lista'):
    itens = st.text_input("Escreva uma meta:", placeholder="Ex: Atingir minha meta de ingestão de água...")
    enviado = st.form_submit_button("Adicionar meta")
    
    if enviado and itens:
        # Adiciona a nova meta à lista no estado da sessão
        st.session_state.lista_itens.append(itens)
        st.success(f'Meta "{itens}" adicionada com sucesso!')

# Chamando a função para marcar os itens
st.header("Suas metas para hoje:")
itens_selecionados = marcar_itens(st.session_state.lista_itens)

# Exibindo a lista de metas e os itens selecionados
if st.session_state.lista_itens:
    if itens_selecionados:
        st.header('- Você concluiu as seguintes metas:')
        for item in itens_selecionados:
            st.write("-", item, "✅")
    else:
        st.info('Nenhuma meta concluída ainda.')
else:
    st.info('Nenhuma meta adicionada ainda.')
