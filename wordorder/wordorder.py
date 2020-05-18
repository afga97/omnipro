

class WordOrder:
    """
        Orden de palabras
        Se le da un archivo de texto con el siguiente formato:

        4
        abcabcdefg abc bcdefg

        La primera línea contiene el número de palabras (n) que tiene el archivo. Las próximasnlíneas contienen palabras (1 por línea), las cuales se pueden repetir a lo largo del archivo. Desarrolle un código que lea la información de dicho archivo de texto, y genere otro archivo de texto con lo siguiente:

            ◦ En la primera línea debe mostrar el número de palabras distintivas.
            ◦ Enlasegundalíneamostrarelnúmerodeocurrenciasdecada palabra distintiva.

        Para el ejemplo anterior, el formato del archivo final es el siguiente:

        3
        2 1 1
    """

    file_url = ""
    file = None
    output_file = "output_file.txt"
    data_output_file = {}

    def __init__(self, file):
        """
            Recibe como parametro la url del archivo .txt a ser leido
        """

        self.file_url = file

    def _open_file(self):
        """
            Abrir el archivo indicado y conceder permisos de lectura.
        """

        try:
            self.file = open(self.file_url, "r+")
        except Exception as e:
            print('No se encontró un archivo para la ruta especificada. error {}'.format(e))

    def _close_file(self, file):
        """
            Cerrar los archivos para ver reflejado la escritura
        """
        file.close()

    def _read_file(self):
        """
            Se lee el archivo y se validan la cantidad de palabras repetidas y cuales no.
        """

        self._open_file()
        count_distinct_letter = 0
        if self.file:
            #TODO readlines es recomendado con archivos pequeños ya que esto se carga en memoria
            fl = self.file.readlines() 
            for f in range(1, len(fl)):
                value = fl[f].rstrip('\n')
                if value in self.data_output_file:
                    self.data_output_file[value] = self.data_output_file[value] + 1
                else:
                    self.data_output_file.update({ value : 1 })
                    count_distinct_letter += 1                
            self.data_output_file.update({ 'count_distinct_letter': count_distinct_letter })
            self._close_file(self.file)
        else:
            print ('No fue posible leer el archivo.')

    def _write_file_output(self):
        """
            Se crea el archivo de salida, se conceden permisos de escritura y se procede a escribir
            la información de cada palabra.
        """
        
        file_output = open(self.output_file, 'w+')
        file_output.truncate(0)
        file_output.write("{}\n".format(str(self.data_output_file['count_distinct_letter'])))
        for key, value in self.data_output_file.items():
            if key != 'count_distinct_letter':
                file_output.write(str(value))
        self._close_file(file_output)

    def main(self):
        try:
            self._read_file()
            self._write_file_output()
        except Exception as e:
            print(e)

instance_word_order = WordOrder('input_file.txt')
instance_word_order.main()