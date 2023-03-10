from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import fire
engine = create_engine("sqlite:///cookbook.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipe'

    recipe_id = Column(Integer, primary_key=True)
    recipe_name = Column(String)
    total_cook_time = Column(String)
    is_vegetarian = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    instructions_id = Column(Integer, ForeignKey('instructions.instruction_id'), nullable=False)

    user = relationship('User', backref='recipes')
    instructions = relationship('Instructions', backref='recipes')
    ingredients = relationship("Recipe_Ingredient", back_populates="recipe")

    def __repr__(self):
        return f'<Recipe {self.recipe_name}>'


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return f'<User {self.user_name}>'


class Instructions(Base):
    __tablename__ = 'instructions'

    instruction_id = Column(Integer, primary_key=True)
    instruction_details = Column(String)

    def __repr__(self):
        return f'<Instructions {self.instruction_id}>'


class Recipe_Ingredient(Base):
    __tablename__ = 'recipe_ingredient'

    recipe_id = Column(Integer, ForeignKey('recipe.recipe_id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)
    quantity = Column(Integer)

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipes")


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    recipes = relationship("Recipe_Ingredient", back_populates="ingredient")

Base.metadata.create_all(engine)
session = Session()
# Get the recipe you want to delete
madison = session.query(User).filter_by(first_name='Madison').first()
session.delete(madison)
session.commit()

# example of fire
def project(fruit):
    fruits = ['apple','cherry','pear','banana']
    fruits.append(fruit)
    print(fruits)

if __name__ == '__main__':
    fire.Fire(project)
    