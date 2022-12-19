import requests
from bs4 import BeautifulSoup
import json


class ExtractWords:

    def __init__(self, type_words: str, link_web: list,) -> None:
        self.links = link_web
        self.type = type_words
        self.words = {self.type: []}

    """
        check_link: Verifica si es que el requests del link nos da un error
    """

    def check_link(self, link):
        content = requests.get(link)
        if content.status_code != 200:
            return ""
        return content.content

    """
        extract_words: Extrae las palabras de cada tabla encontrada en el html de la página web
    """

    def extract_words(self):
        for link in self.links:
            content = self.check_link(link)

            if not content:  # Si content es vacío, nos devuelve el link que no se pudo obtener
                return {"error": {"Type": self.type, "Link": link}}

            content_html = BeautifulSoup(content, "lxml")
            tables = content_html.find_all(
                "div", attrs={'class': 'theme-table su_table'})  # Encontramos todas las etiquetas tables
            for table in tables:  # Recorre las tablas
                # encuentra todas las etiquetas tr(filas)
                rows = table.find_all("tr")
                for row in rows:  # Recorre todas las filas
                    column = row.find_all("td")  # Obtiene las columnas
                    for cell in column:  # recorre cada columna
                        word: str = cell.get_text()  # Extrae el texto de la etiqueta td
                        if u"\xa0" in word:  # Elimina caracteres especiales
                            word = word.replace(u"\xa0", u"")
                        word_upper = word.upper()
                        self.words[self.type].append(word_upper)

        return self.words


def main():
    links_web = {
        "Animales": ["https://www.ejemplos.co/palabras-graves-de-animales/",
                     "https://www.ejemplos.co/palabras-agudas-de-animales/"],
        "Frutas": ["https://www.ejemplos.co/palabras-graves-de-frutas/",
                   "https://www.ejemplos.co/palabras-agudas-de-frutas-y-verduras/"],
        "Países": ["https://www.ejemplos.co/palabras-graves-de-paises/",
                   "https://www.ejemplos.co/palabras-agudas-de-paises/"]
    }

    data = dict()
    # Lista de objetos
    word_type_objects = [ExtractWords(i, j) for i, j in links_web.items()]
    for dict_words in word_type_objects:
        words = dict_words.extract_words()
        if not words:
            print(words)  # Imprime si es que se encontró el error
        data.update(words)

    with open("words.json", "w", encoding="utf-8") as file:
        # ensure_ascii, para usar los ascii real
        json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
