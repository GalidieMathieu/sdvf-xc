use spot;
set sql_safe_updates=0;

#------------------------------------------------------------Création des deux tables importantes------------------------------------------------------------
DROP TABLE IF EXISTS data_recommendation_system;
DROP TABLE IF EXISTS favorite_recipes;
DROP TABLE IF EXISTS prenium_unlock;
DROP TABLE IF EXISTS premium;
DROP TABLE IF EXISTS regime_recette;
DROP TABLE IF EXISTS regime_users;
DROP TABLE IF EXISTS regime_alimentaire;
DROP TABLE IF EXISTS ingredient_in_recipe;
DROP TABLE IF EXISTS relation_ingredient_user;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS ingredient;
DROP TABLE IF EXISTS ingredient_type;
DROP TABLE IF EXISTS recipes;

CREATE TABLE IF NOT EXISTS Recipes (
    ID int NOT NULL PRIMARY KEY auto_increment,
    nom varchar(255) NOT NULL,
    temps int not null,
    nbPersonnes int not null,
    Directions text not null
); 

CREATE TABLE IF NOT EXISTS Users (
    ID int NOT NULL PRIMARY KEY auto_increment,
    Pseudo varchar(255) NOT NULL,
    PasswordUser binary(20) not null,
    mail_adress varchar(255) not null
); 

CREATE TABLE IF NOT EXISTS Favorite_recipes(
	IDUsers int NOT NULL,
    IDRecipes int NOT NULL,
    type_fav varchar(255) not null,
    FOREIGN KEY (IDUsers) REFERENCES Users(ID),
    FOREIGN KEY (IDRecipes) REFERENCES Recipes(ID)
);

CREATE TABLE IF NOT EXISTS data_recommendation_system(
	IDUsers int NOT NULL,
    IDRecipes int NOT NULL,
    nbrVue int NOT NULL,
    nbrClick int NOT NULL,
    rating float,
    FOREIGN KEY (IDUsers) REFERENCES Users(ID),
    FOREIGN KEY (IDRecipes) REFERENCES Recipes(ID)
);

#------------------------------------------------------------Tables Regimes------------------------------------------------------------
# Regime_Alimentaire | regime_users , regime_recette

CREATE TABLE IF NOT EXISTS Regime_Alimentaire  (
    ID int NOT NULL PRIMARY KEY auto_increment,
    nom varchar(255) NOT NULL
); 

#liason
CREATE TABLE IF NOT EXISTS regime_users (
	IDUser int NOT NULL ,
    IDRegime int NOT NULL,
    allergie Bool NOT NULL,
    FOREIGN KEY (IDUser) REFERENCES Users(ID),
    FOREIGN KEY (IDRegime) REFERENCES Regime_Alimentaire(ID)
);

CREATE TABLE IF NOT EXISTS regime_recette (
	IDRecipe int NOT NULL ,
    IDRegime int NOT NULL,
    FOREIGN KEY (IDRecipe) REFERENCES Recipes(ID),
    FOREIGN KEY (IDRegime) REFERENCES Regime_Alimentaire(ID)
);

#------------------------------------------------------------Tables Ingredient------------------------------------------------------------
# Ingredient, Ingredient_Type | Ingredient_In_Recipe, Is_Type_Ingredient, relation_Ingredient_User
CREATE TABLE IF NOT EXISTS Ingredient_Type (
    ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Ingredient (
    ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom varchar(255) NOT NULL,
    unite varchar(255) NOT NULL,
    IDTypeIngredient int NOT NULL,
    FOREIGN KEY (IDTypeIngredient) REFERENCES Ingredient_Type(ID)
); 



#liaison avec ingrédients
CREATE TABLE IF NOT EXISTS Ingredient_In_Recipe (
	IDIngredient int NOT NULL ,
    IDRecipe int NOT NULL,
    quantite float NOT NULL,
    optionnel bool NOT NULL,
    FOREIGN KEY (IDIngredient) REFERENCES Ingredient(ID),
    FOREIGN KEY (IDRecipe) REFERENCES Recipes(ID)
); 

CREATE TABLE IF NOT EXISTS relation_Ingredient_User(
	IDIngredient int NOT NULL,
	IDUser int NOT NULL,
    FOREIGN KEY (IDIngredient) REFERENCES Ingredient(ID),
    FOREIGN KEY (IDUser) REFERENCES Users(ID)
);

#------------------------------------------------------------Premium------------------------------------------------------------
CREATE TABLE IF NOT EXISTS premium (
    ID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    formule varchar(255) NOT NULL,
    fonctionnalite varchar(255) NOT NULL,
    debut date NOT NULL,
    fin date NOT NULL
);

CREATE TABLE IF NOT EXISTS Prenium_Unlock (
	IDPremium int NOT NULL,
	IDUser int NOT NULL,
    FOREIGN KEY (IDPremium) REFERENCES premium(ID),
    FOREIGN KEY (IDUser) REFERENCES Users(ID)
);
