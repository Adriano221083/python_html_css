from  flask  import  Flask , render_template , g , request , flash , session , redirect , url_for , abort
importar  sqlite3

DATABASE  =  "banco.bd"
SECRET_KEY  =  "chave"

app  =  Flask ( "Olá" )
aplicativo . configuração . from_object ( __name__ )

def  conecta_bd ():
    retorne  sqlite3 . conectar ( BANCO DE DADOS )

@aplicativo . _ pedido_antes
def  antes_requisicao ():
    g . bd  =  conecta_bd ()

@aplicativo . _ solicitação de desmontagem
def  depois_requisicao ( e ):
    g . bd . fechar ()

@aplicativo . _ rota ( "/" )
def  exibir_entradas ():
    sql  =  "SELECT titulo, texto, criado_em FROM entradas ORDER BY id DESC;"
    cur  =  g . bd . executar ( sql )
    entradas  = []
    para  titulo , texto , criado_em  in  cur . buscar tudo ():
        entradas . append ({ "titulo" : titulo , "texto" : texto , "criado_em" : criado_em })
    return  render_template ( "exibir_entradas.html" , entradas = entradas )

@aplicativo . _ rota ( '/inserir' , métodos = [ "POST" ])
def  inserir_entradas ():
    se  não  sessão . get ( 'logado' ):
        abortar ( 401 )
    titulo  =  pedido . formulário [ 'título' ]
    texto  =  pedido . formulário [ 'texto' ]
    sql  =  "INSERT INTO entradas(título, texto) VALUES (?,?)"
    g . bd . execute ( sql , [ titulo , texto ])
    g . bd . cometer ()  
    flash ( "Nova entrada com sucesso!" )
     redirecionamento de retorno ( url_for ( "exibir_entradas" ))

@aplicativo . _ route ( '/login' , métodos = [ "GET" , "POST" ])
def  login ():
    erro  =  Nenhum
    se  solicitar . método  ==  "POST" :
        se  solicitar . form [ 'username' ] ==  "admin"  e  request . form [ 'senha' ] ==  "admin" :
            sessão [ 'logado' ] =  Verdadeiro
            flash ( "Login calculado!" )
             redirecionamento de retorno ( url_for ( 'exibir_entradas' ))
        erro  =  "Usuário ou Senha inválidos"
    return  render_template ( "login.html" , erro = erro )

@aplicativo . _ rota ( "/logout" )
def  sair ():
    sessão . pop ( 'logado' , Nenhum )
    flash ( "Logout Efetuado com Sucesso!" )
     redirecionamento de retorno ( url_for ( "exibir_entradas" ))