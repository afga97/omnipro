import json

products = {
    'Producto1': {
        'name': 'Zapatos XYZ',
        'barcode': '8569741233658',
        'supplier': 'DeportesXYZ',
        'category': 'Zapatos',
        'gender': 'Masculino'
    },
    'Producto2': {
        'name': 'Zapatos ABC',
        'barcode': '7452136985471',
        'supplier': 'DeportesXYZ',
        'category': 'Zapatos',
        'gender': 'Femenino'
    },
    'Producto3': {
        'name': 'CamisaDEF',
        'barcode': '5236412896324',
        'supplier': 'DeportesXYZ',
        'category': 'Camisas',
        'gender': 'Masculino'
    },
    'Producto4': {
        'name': 'Bolso KLM',
        'barcode': '5863219635478',
        'supplier': 'CarterasHi-Fashion',
        'category': 'Bolsos',
        'gender': 'Femenino'
    }
}



class GroupObjects:
    """
        Agrupación deobjetos
        Dado una serie de productos con los siguientes parámetros:

        ◦ Nombre (Letras y números)
        ◦ Código de barras (sólo números)
        ◦ Fabricante (sólo letras)
        ◦ Categoría (sólo letras)
        ◦ Género (Masculino o Femenino)
    """


    data_products = {}
    data_output = {}

    def __init__(self, data):
        self.data_products = data

    def group_products(self):
        """
            Itera el diccionario de productos y se categoriza por proveedor, categoria y genero.
        """
        for product, data in self.data_products.items():
            if data['supplier'] in self.data_output.keys():
                if data['category'] in self.data_output[data['supplier']]:
                    if data['gender'] in self.data_output[data['supplier']][data['category']]:
                        self.data_output[data['supplier']][data['category']][data['gender']].append(product)
                    else:
                        self.data_output[data['supplier']][data['category']].update({
                            data['gender']: [ product ]
                        })
                else:
                    self.data_output[data['supplier']].update( 
                        { 
                            data['category']: { 
                                data['gender']: [ product ] 
                            } 
                        }
                    )
            else:
                self.data_output.update({ 
                    data['supplier']: { 
                        data['category']: { 
                            data['gender']: [ product ]
                        } 
                    } 
                })

    def write_output_data(self):
        """
            Imprime los productos categorizados en un dict.
        """
        print(json.dumps(self.data_output, sort_keys=False, indent=5))

    def main(self):
        try:
            self.group_products()
            self.write_output_data()
        except Exception as e:
            print('Ocurrio un error. {}'.format(e))


instance_group = GroupObjects(products)
instance_group.main()


