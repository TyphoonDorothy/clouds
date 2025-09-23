from .ingredient_routes import ingredient_bp
from .dish_routes import dish_bp
from .sportsman_routes import sportsman_bp
from .doctors_contact_routes import doctors_contact_bp
from .doctor_specialization_routes import doctor_specialization_bp
from .supplement_routes import supplement_bp
from .doctor_routes import doctor_bp
from .coach_specialization_routes import coach_specialization_bp
from .coach_routes import coach_bp
from .coaches_contact_routes import coaches_contact_bp
from .program_routes import program_bp
from .sportsman_has_supplement_routes import sportsman_has_supplement_bp
from .sportsman_has_program_routes import sportsman_has_program_bp
from .program_has_dish_routes import program_has_dish_bp
from .dish_has_ingredient_routes import dish_has_ingredient_bp

def register_routes(app):
    app.register_blueprint(ingredient_bp, url_prefix="/api")
    app.register_blueprint(dish_bp, url_prefix="/api")
    app.register_blueprint(sportsman_bp, url_prefix="/api")
    app.register_blueprint(doctors_contact_bp, url_prefix="/api")
    app.register_blueprint(doctor_specialization_bp, url_prefix="/api")
    app.register_blueprint(supplement_bp, url_prefix="/api")
    app.register_blueprint(doctor_bp, url_prefix="/api")
    app.register_blueprint(coach_specialization_bp, url_prefix="/api")
    app.register_blueprint(coach_bp)
    app.register_blueprint(coaches_contact_bp, url_prefix="/api")
    app.register_blueprint(program_bp, url_prefix="/api")
    app.register_blueprint(sportsman_has_supplement_bp, url_prefix="/api")
    app.register_blueprint(sportsman_has_program_bp, url_prefix="/api")
    app.register_blueprint(program_has_dish_bp, url_prefix="/api")
    app.register_blueprint(dish_has_ingredient_bp, url_prefix="/api")