console.log(`testando
a
multi
linha 

`)

console.log(`Soma no JS faz assim: ${1+1}` ) // template literals ou template strings
console.log("Soma: 1+1= ${}", 1+1)

/*
    Boolean
  True or false

    Undefined <> Null
  Null == [] (conjunto vazio)
*/

console.log(undefined === null) // ele mostra "false".

/*
    Object
  Propriedades / Atributos
  Funcionalidades / Métodos
*/

// console (de console.log()) é um objeto o que me faz pensar em "função ou comando".
// chama-se um objeto fazendo: { propriedade: "valor" }

console.log({
    name: "Maykão",
    idade: 17,
    pular: function() {
        console.log('jump')
    },
    altura: 1.915
})  // Acho que aqui ele criou uma variável como no Python -> x= input("Diga seu nome: ")

/*
    Array (vetores)
  Lista 
*/

console.log(["Mayk",
"Jonel", 
33, 
])

/*
    \\\ Veredito: ///
    Data Types:
  Primitivos, estruturais e Pe.
    P=  Str, Num, Boolean, Array, undefined, Symbol and BigInt.
    e=  Obj {Array, Map, Set, Date}, Function. 
    Pe= Null. 
*/

// "=" é ...; "==" ; "===" comparativo.