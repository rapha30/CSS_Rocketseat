/*
    Variáveis:
  var
  let
  const
*/

var clima= "Quente"
console.log(clima)
console.log(typeof clima)

/*
    Var é global e local.
  hoisting = "elevação"
*/

{
console.log('Existe X antes do bloco? ', x); // mesmo não ainda criada existe, mas sem valor.

{
  var x= 0
}

console.log(`Existe X depois do bloco? ${x}`);
}

// Com const e let <>

{
 
  console.log(`existe x antes do escopo? ${x}`);
  {
    const x= 0
    console.log(`Existe o x do bloco? ${x}`);
  }
  

}