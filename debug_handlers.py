from flask import Flask
from flask import request
import json

from pony.orm import Database

app = Flask(__name__)

#-BEGIN CUSTOM HANDLERS



def _sample1_on_create():
    if not hashMap.containsKey("a"):
        hashMap.put("a","")    
    if not hashMap.containsKey("b"):
        hashMap.put("b","")        
    return hashMap



def _sample1_on_input():
    if hashMap.get("listener")=="btn_res":
        sum=int(hashMap.get("a"))+int(hashMap.get("b"))
        hashMap.put("toast",str(int(hashMap.get("a"))+int(hashMap.get("b"))))
    return hashMap


def stock_on_create_buy(hash_map, _files=None, _data=None):
    table_buy = {
        "type": "table",
        "textsize": "17",

        "columns": [
            {
                "name": "buy",#cell",
                "header": "Ячейка",
                "weight": "2"
            },
            {
                "name": "num",
                "header": "number", #Товар",
                "weight": "1"
            }
        ]
    }

    """
    Open the database with required tables
    """

    DB_PATH = 'sqlite_dev.db'
    db = Database()

    if hash_map:
        db_path = hash_map.get('DB_PATH')

    db.bind(provider='sqlite', filename=db_path, create_db=False)
    db.generate_mapping(create_tables=False)

    if Buy.len() == 0:
        Buy[0].
        order.set(state="Shipped", date_shipped=datetime.now())
        .commit()


    rows = []
    for record in results:
        rows.append({"buy": record[0], "num": record[1]})

    table_buy['rows'] = rows
    hash_map.put("table_buy", json.dumps(table_buy))

    return hash_map


def stock_input(hashMap, _files=None, _data=None):
    if hashMap.get("listener") == "barcode":

        nom = ui_global.SW_Goods.get(barcode=hashMap.get("barcode"))
        is_nom = False

        object = ""

        if nom == None:
            is_nom = False
        else:
            is_nom = True
            hashMap.put("object", nom.name)
            hashMap.put("table_object", get_table_by_nom(nom.id))
            hashMap.put("ShowScreen", "Остатки по объекту")

        if not is_nom:
            cell = ui_global.SW_Cells.get(barcode=hashMap.get("barcode"))
            if cell == None:
                hashMap.put("toast", "Штрихкод ни ячейки ни тоара")
            else:
                hashMap.put("object", cell.name)
                hashMap.put("table_object", get_table_by_cell(cell.id))
                hashMap.put("ShowScreen", "Остатки по объекту")

#-END CUSTOM HANDLERS

@app.route('/set_input_direct/<method>', methods=['POST'])
def set_input(method):
    func = method
    jdata = json.loads(request.data.decode("utf-8"))
    f = globals()[func]
    hashMap.d=jdata['hashmap']
    f()
    jdata['hashmap'] = hashMap.export()
    jdata['stop'] =False
    jdata['ErrorMessage']=""
    jdata['Rows']=[]

    return json.dumps(jdata)

@app.route('/post_screenshot', methods=['POST'])
def post_screenshot():
    d = request.data
    return "1"

class hashMap:
    d = {}
    def put(key,val):
        hashMap.d[key]=val
    def get(key):
        return hashMap.d.get(key)
    def remove(key):
        if key in hashMap.d:
            hashMap.d.pop(key)
    def containsKey(key):
        return  key in hashMap.d
    def export(key):
        ex_hashMap = []
        for key in hashMap.d.keys():
            ex_hashMap.append({"key":key,"value":hashMap.d[key]})
        return ex_hashMap

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=2075,debug=True)