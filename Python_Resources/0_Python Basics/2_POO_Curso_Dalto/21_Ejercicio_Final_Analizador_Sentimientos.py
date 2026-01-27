from textblob import TextBlob

class AnalizadoDeSentimiento():
    def analizar_sentimiento(self,texto):
        texto=texto.lower()
        analisis=TextBlob(texto)
        print(analisis.sentiment)
        if analisis.sentiment.polarity == 0:
            return "neutral"
        elif analisis.sentiment.polarity<0:
            return "Negativo"
        else:
            return "Positivo"
    
analizador=AnalizadoDeSentimiento()
resultado=analizador.analizar_sentimiento("I am depressed")
print(resultado)

