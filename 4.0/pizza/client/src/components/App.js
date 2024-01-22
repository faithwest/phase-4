import React from 'react';
import { BrowserRouter, Routes , Route} from 'react-router-dom';
import pizza from './Pizza';
import PizzasList from './PizzasList';
import RestaurantsList from './RestaurantsList';
import RestaurantDescription from "./RestaurantDescription";
import RestaurantPizzas from "./RestaurantPizzas";



function App() {
  return (
    <div>
    <BrowserRouter>
    <Routes>

    <Route exact path="/restaurants/:id" components={<RestaurantDescription />} />
    <Route path="/" components ={RestaurantsList} />
    <Route path="/pizza" components={pizza} />
    <Route path="/pizzas" components={PizzasList} />
    <Route path="/restaurantpizzas" components={<RestaurantPizzas/>}/>

      
    </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
