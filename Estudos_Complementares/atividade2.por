programa
{
    funcao inicio()
    {
        inteiro i = 2
        escreva("Valor de i antes de chamar a funcao: ", i, "\n")
        contarRepeticao(i)
        escreva("Valor de i depois de chamar a funcao: ", i, "\n")
    }
    funcao contarRepeticao(inteiro &i){
    {
        escreva("Valor de i dentro da funcao repeticao: \n")
        faca {
            escreva(i++*2, "\n")
        } enquanto (i < 10)

} 
        