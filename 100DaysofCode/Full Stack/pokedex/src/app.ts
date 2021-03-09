//  due to | Union type we can have multiple types
const container: HTMLElement | any = document.getElementById("app");
const pokemons: number = 100;
//  Ipokemon defines the shape of the object

interface IPokemon {
  id: number;
  name: string;
  image: string;
  type: string;
}

// this loop over the each pokemon and retrieves the number of pokemon
const fetchData = (): void => {
  for (let i = 1; i <= pokemons; i++) {
    getPokemon(i);
  }
};

//  Asynchronous func.
const getPokemon = async (id: number): Promise<void> => {
  const data: Response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
  const pokemon: any = await data.json();
  const pokemonType: string = pokemon.types
    .map((poke: any) => poke.type.name)
    .join(", ");

  const transformedPokemon = {
    id: pokemon.id,
    name: pokemon.name,
    image: `${pokemon.sprites.front_default}`,
    type: pokemonType
  };

  showPokemon(transformedPokemon);
};

const showPokemon = (pokemon: IPokemon): void => {
  let output: string = `
  <div class = "scene">
  <div class="card">
  <div class= "card__face card__face--front">
  <span class="card--id">#${pokemon.id}</span>
  <img class="card--image" src=${pokemon.image} alt=${pokemon.name} />
  <h1 class="card--name">${pokemon.name}</h1>
  <span class="card--details">${pokemon.type}</span>
  </div>
    <div class = "card__face card__face--back">
            <span class="card--details">${pokemon.type}</span></div>   
        </div>
  </div>
        
    `;
  container.innerHTML += output;
};

fetchData();