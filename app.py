import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown("""
<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} </style>
""", unsafe_allow_html=True) 

st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
""", unsafe_allow_html=True)

st.title("Semantic Search")


@st.experimental_singleton
def init_retriever():
    print("Singleton init_retriever")
    # initialize retriever model
    #return SentenceTransformer('pinecone/mpnet-retriever-squad2')


def card(id_val, source):
    st.markdown(f"""
    <div class="card" style="margin:1rem;">
        <div class="card-body">
            <h6 class="card-subtitle mb-2 text-muted">{id_val}</h6>
            <h5 class="card-title">{source}</h5>            
        </div>
    </div>
    """, unsafe_allow_html=True)


# initialize the index and retriever components
retriever = init_retriever()


query = st.text_input("Enter something to search", "")
if query != "":
    print("Query:", query)
    # encode the query as sentence vector
    #xq = retriever.encode([query]).tolist()    
    # get relevant contexts
    #xc = index.query(xq, top_k=5,
    #                 include_metadata=True)
    xc = {"results":[{"matches": [{"id":1, "metadata":{"title": query, "text": "test"}},
    {"id":2, "metadata":{"title":query, "text": "test"}},
    {"id":3, "metadata":{"title":query, "text": "test"}}
    ]}]}

    # display each context (NEW PART)
    for context in xc['results'][0]['matches']:
        card(
            context['id'],
            context['metadata']['title']
        )
st.markdown("""---""")
st.markdown("""<h6 class="card-subtitle mb-2 text-muted">Please reach out to xxx for any questions.</h6>""", unsafe_allow_html=True)
