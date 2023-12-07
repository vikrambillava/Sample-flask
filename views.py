from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, roles_required
from datetime import datetime


class PurchaseAnalytics(Resource):
    @login_required
    @roles_required('PM', 'RM')
    def get(self):
        start_date = datetime(2023, 11, 30)
        end_date = datetime(2023, 12, 7)

        city = 'YourCity'

        result = (
            db.session.query(Inventory.product_name, db.func.count().label('purchase_count'))
            .filter(Activity_Customer.Time Series - Timestamp.between(start_date, end_date))
            .filter(Inventory.warehouse == city)
            .group_by(Inventory.product_name)
            .order_by(db.func.count().desc())
            .limit(10)
            .all()
        )

        response = [{"product_name": row.product_name, "purchase_count": row.purchase_count} for row in result]
        return jsonify(response)

api = Api(app)
api.add_resource(PurchaseAnalytics, '/purchase-analytics')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)