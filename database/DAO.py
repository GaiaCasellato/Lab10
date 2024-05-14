from database.DB_connect import DBConnect
from model.Contiguity import Contiguity
from model.Country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountryYearNodes(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct con.state1ab as StateAbb, con.state1no as CCode , c.StateNme 
                    from contiguity con, country c 
                    where con.year <= %s and con.state1no = c.CCode """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Country(**row))


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllContiguityYearEdges(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from contiguity c 
                    where c.year <= %s and c.conttype = 1"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Contiguity(**row))

        cursor.close()
        conn.close()
        return result




