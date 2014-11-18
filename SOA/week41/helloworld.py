from flask import Flask,  request
from flask.ext.restful import Api, Resource
import riak

app = Flask(__name__)
api = Api(app)

myClient = riak.RiakClient(protocol='http', host='192.168.122.110', http_port=8098)

class AddContact(Resource):
    def post(self):
        phone = request.form['phone']
        name = request.form['name']
        myBucket = myClient.bucket('contact')
        contactInfo = myBucket.new(name, data=phone)
        contactInfo.store()
        print 'contact stored'
        return {'name':name,  'phone':phone }

class SearchContact(Resource):
    def get(self, searchName):
        myBucket = myClient.bucket('contact')
        fetched = myBucket.get(searchName)
        print fetched.data
        if fetched.data != None:
            phoneRetrieved = fetched.data
            print 'retrieved data'
            return {'Status' : 'Retrieved Success',  'name':searchName,  'phone':phoneRetrieved}
        else:
            print 'not exists'
            return{'Status' : 'None Exist Contact',  'name':'',  'phone':''}

api.add_resource(AddContact, '/add')
api.add_resource(SearchContact,  '/search/<string:searchName>')

if __name__ == '__main__':
    app.run(debug=True)
