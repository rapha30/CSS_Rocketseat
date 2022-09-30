#   Valores e unidades de medidas
```css
/*
    Cada propriedade possui valores 
    Como conhecer e estudar os valores na documentação?
        Documentação MDN: https://developer.mozilla.org/en-US/
*/
property: value

<color> <length>

Os termos podem variar values ou data types
```
------------------------------------------------------------------------------------------------------------
#   Tipos numéricos

<integer> - número inteiro como -10 ou 223
<number> - número decimal como -2.4, 64 ou 0.234
** <dimension> - é um <number> com uma unidade junto: 90deg, 2s, 8px
<percentage> - representa uma fração de outro número: 50%

##  Unidades comuns

** <length> - é um dos mais usados no CSS e representa um valor de distância: px, em, vw
<angle> - representa um ângulo: deg, rad, turn
<time> - representa um tempo: s, ms
** >Responsive< <resolution> - representa resoluções para dispositivos: dpi

------------------------------------------------------------------------------------------------------------

#   Distâncias absolutas <length>
```css
São fixas e não alteram seu valor.

| Unidade  | Nome                | Equivalência         |
|----------|---------------------|----------------------|
| cm       | Centímetros         | 1cm = 96px/2.54      | 
| in       | Inches (polegadas)  | 1in = 2.54cm = 96px  | 
| px       | Pixels              | 1px = 1/96th of 1in  |
*o mais comum e mais utilizado é o px

*não é recomendado usar cm

 Distâncias relativas

São relativas a um outro valor, pode ser o elemento pai, ou root, ou o tamanho da tela.
Benefício: Maior adaptação aos diferentes tipos de tela.
| Unidade  | Relativo a                                    |
|----------|-----------------------------------------------|
| em       | Tamanho da font do elemento pai               |
| rem      | Tamanho da font do elemento raiz (root/html)  | 
| vw       | 1% da viewport wid                            |  
| vh       | 1% da viewport height                         |
Normalmente o tamanho da font padrão do navegador é de 16px e para mudar esse valor temos que fazer a alteração no root ou no elemento html.
:root {
	font-size: 18px;
}

/* OU */

html {
	font-size: 18px;
}
O viewport é a parte da tela que está sendo exibida. No caso dos navegadores web, é o que é exibido na janela/tela do documento. Conteúdos que estão fora do viewport só serão exibidos quando feito um scroll da área de visualização.