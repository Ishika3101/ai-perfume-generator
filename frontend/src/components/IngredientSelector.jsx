import { useState } from "react"
import ingredients from "../data/ingredients"

export default function IngredientSelector({ onSelect }) {

  const [selected, setSelected] = useState([])
  const [search, setSearch] = useState("")

  function toggleIngredient(ingredient) {

    let updated

    if (selected.includes(ingredient)) {
      updated = selected.filter(i => i !== ingredient)
    } else {
      updated = [...selected, ingredient]
    }

    setSelected(updated)
    onSelect(updated)
  }

  const filteredIngredients = ingredients.filter((ing) =>
    ing.toLowerCase().includes(search.toLowerCase())
  )

  return (
    <div className="bg-white/20 backdrop-blur-md p-6 rounded-xl h-[500px] overflow-hidden">

      <h2 className="text-xl font-bold mb-3">Ingredient Lab</h2>

      {/* Search box */}
      <input
        type="text"
        placeholder="Search ingredient..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="w-full mb-3 p-2 rounded bg-white/30 outline-none"
      />

      {/* Ingredient list */}
      <div className="h-[380px] overflow-y-scroll space-y-2">

        {filteredIngredients.map((ingredient) => (

          <label key={ingredient} className="flex items-center space-x-2">

            <input
              type="checkbox"
              checked={selected.includes(ingredient)}
              onChange={() => toggleIngredient(ingredient)}
            />

            <span>{ingredient}</span>

          </label>

        ))}

      </div>

    </div>
  )
}