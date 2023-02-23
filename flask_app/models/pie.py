from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = 'belt_exam_erd'

class Pie:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['pie_name']
        self.filling = data['filling']
        self.crust = data['crust']
        self.created_at = data['created_at']        
        self.updated_at = data['updated_at']
        self.votes = data['votes']       

    @classmethod
    def save_recipie(cls, data):
        query = 'INSERT INTO pies (created_at, updated_at, user_id , pie_name, filling, crust) VALUES (NOW(),NOW(),%(user_id)s,%(pie_name)s, %(filling)s, %(crust)s);'
        return connectToMySQL(mydb).query_db(query,data)

    @staticmethod
    def validate_pie(pie):
        print (pie)
        is_valid = True
        if len(pie['pie_name']) < 1:
            flash("Please enter a pie name")
            is_valid = False
        if len(pie['filling']) < 1:
            flash("Please enter a pie filling.")
            is_valid = False
        if len(pie['crust']) < 1:
            flash("Please enter a pie crust.")
            is_valid = False
        return is_valid

    @staticmethod
    def getAllPies():
        pies = []
        query = '''
        SELECT * FROM pies
        LEFT JOIN users on users.id = pies.user_id
        ORDER BY votes DESC;
        '''
        results = connectToMySQL(mydb).query_db(query)
        #print(results)
        #for row in results:
        #    print(row)
        #    pies.append(row)
        return results

    @classmethod
    def delete(cls, id):
        query = '''
        DELETE FROM pies 
        WHERE id = %(id)s;
        '''
        return connectToMySQL(mydb).query_db(query,id)
    
    @classmethod
    def getPieByID(cls, id):
        pies = []
        query = '''
        SELECT *
        FROM pies
        WHERE user_id = %(id)s;
        
        '''
        results = connectToMySQL(mydb).query_db(query,id)
        for row in results:
            pies.append(row)
        #print(pies)
        return pies
    @classmethod
    def getPieByPID(cls, id):
        query = '''
        SELECT *
        FROM pies
        WHERE id = %(id)s;
        
        '''
        results = connectToMySQL(mydb).query_db(query,id)
        #print(results)
        return results[0]

    @classmethod
    def edit(cls, id):
        query = '''
        UPDATE pies
        SET pie_name = %(pie_name)s,
        filling = %(filling)s,crust = %(crust)s,
        updated_at = NOW()
        WHERE id = %(id)s;
        '''
        return connectToMySQL(mydb).query_db(query,id)

    @classmethod
    def getPieInfo(cls, id):
        query = '''
        SELECT *
        FROM pies
        LEFT JOIN users on users.id = pies.user_id
        WHERE pies.id = %(id)s;
        '''
        results = connectToMySQL(mydb).query_db(query,id)
        return results[0]
    
    @classmethod
    def vote(cls, data):
        query = '''
        INSERT INTO votes (users_id, pie_id)
        VALUES (%(user_id)s, %(pie_id)s)
        '''
        return connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def getVotes(cls, data):
        query = '''
        SELECT *
        FROM votes
        JOIN pies on pies.id = votes.pie_id
        WHERE pie_id = %(pie_id)s;
        '''
        results = connectToMySQL(mydb).query_db(query,data)
        cls.votes = len(results)
        print(cls.votes)
        return connectToMySQL(mydb).query_db(query,data)



    @classmethod
    def checkVote(cls, data):
        query = '''
        SELECT *
        FROM votes
        where users_id = %(id)s
        AND pie_id = %(pie_id)s;
        '''
        results = connectToMySQL(mydb).query_db(query,data)
        print (len(results))

        return len(results)

    @classmethod
    def removeVote(cls, data):
        query = '''
        DELETE FROM votes
        WHERE users_id = %(user_id)s
        AND pie_id = %(pie_id)s;
        '''

        return connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def removeVote(cls, data):

        query = '''
        DELETE FROM votes
        WHERE users_id = %(user_id)s
        AND pie_id = %(pie_id)s;
        '''

        return connectToMySQL(mydb).query_db(query,data)

    @classmethod
    def deleteVote(cls, data):
        query = '''
        UPDATE pies
        SET votes = %(votes)s
        WHERE id = %(pie_id)s;        
        
        '''
        return connectToMySQL(mydb).query_db(query,data)
    @classmethod
    def addvote(cls, data):
        query = '''
        UPDATE pies
        SET votes = %(votes)s
        WHERE id = %(pie_id)s;        
        
        '''
        return connectToMySQL(mydb).query_db(query,data)
