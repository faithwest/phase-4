import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function RestaurantsList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch('/restaurants')
      .then(response => response.json())
      .then(data => setRestaurants(data));
  }, []);

  function handleDelete(id) {
    fetch(`/restaurants/${id}`, {
      method: "DELETE",
    }).then((r) => {
      if (r.ok) {
        setRestaurants((restaurants) =>
          restaurants.filter((restaurant) => restaurant.id !== id)
        );
      }
    });
  }

  return (
    <div>
      <h1>Our Restaurants</h1>
      <ul>
        {restaurants.map(restaurant => (
          <li key={restaurant.id}>
            <Link to={`/restaurants/${restaurant.id}`}>{restaurant.name}🍲</Link>
            <p>{restaurant.address}</p>
            <button type="button" onClick={() => handleDelete(restaurant.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <button>
        <Link to="/restaurant_pizzas/new">Add a new Pizza</Link>
      </button>
    </div>
  );
}

export default RestaurantsList;
