# At rules
```css
/*
    São regras relacionadas ao comportamento do CSS, começa com um sinal de @ seguido do identificador e do valor.
*/

@import serve para incluir um CSS externo.
@media são regras condicionais para vários dispositivos.
@font-face é para colocar fontes externas.
@keyframes serve para as animations do CSS.

# Shorthand
```css
/* 
    Junção de propriedades, para que fiquem de forma resumida e legível.
*/

{
    /* background properties */
    background-color: #000;
    background-image: url(images/bg.gif);
    background-repeat: no-repeat;
    background-position: left top;

    /* background shorthand*/
    background: #000 url(images/bg.gif) no-repeat left top;

    /* font properties */
    font-style: italic;
    font-weight: bold;
    font-size: .8em;
    line-height: 1.2;
    font-family: Arial, sans-serif;

    /* font shorthand */ 
    font: bold italic .8em/1.2 Arial, sans-serif;
}
/*
    Algumas das características do shorthand:

    Não irá considerar propriedades anteriores, ou seja, caso faça um shorthand, apenas ele será considerado, quaisquer propriedades anteriores serão substituídas pelas do shorthand.

    Os valores que não forem especificados irão assumir o valor padrão.

    Por fim, geralmente, a ordem descrita não importa, mas, caso haja muitas propriedades com valores semelhantes, poderemos encontrar problemas.
*/

# Funções
```css
/*
    Um tipo de valor existente no CSS, é estruturado com um nome seguido de abre e fecha parênteses.
    Recebe um argumento, que são seus valores.
*/
@import url("http://urlaqui.com/style.css");
color: rgb(255,0,100);
width: calc(100% - 10px);