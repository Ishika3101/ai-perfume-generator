import { useState } from "react"
import { ingredients } from "../data/ingredients"

export default function IngredientSelector(){

const [search,setSearch] = useState("")
const [selected,setSelected] = useState([])

function toggleIngredient(item){

if(selected.includes(item)){
setSelected(selected.filter(i=>i!==item))
}else{
setSelected([...selected,item])
}

}

const filteredIngredients = ingredients.filter(item =>
item.toLowerCase().includes(search.toLowerCase())
)

return(

<div className="bg-white/20 backdrop-blur-xl rounded-2xl p-6 text-white shadow-xl">

<h2 className="text-2xl font-bold mb-4">
Ingredient Lab
</h2>

{/* Search Bar */}

<input
type="text"
placeholder="Search ingredient..."
value={search}
onChange={(e)=>setSearch(e.target.value)}
className="w-full p-2 rounded-lg text-black mb-4"
/>

{/* Selected Ingredient Chips */}

{selected.length > 0 && (

<div className="mb-4">

<p className="text-sm mb-2">
Selected Ingredients
</p>

<div className="flex flex-wrap gap-2">

{selected.map((item)=>(
<div
key={item}
className="px-3 py-1 bg-white text-black rounded-full text-sm cursor-pointer"
onClick={()=>toggleIngredient(item)}
>

{item} ✕
</div>
))}

</div>

</div>

)}

{/* Ingredient List */}

<div className="h-80 overflow-y-auto space-y-2">

{filteredIngredients.map((item)=>(
<label key={item} className="flex items-center gap-2 cursor-pointer">

<input
type="checkbox"
checked={selected.includes(item)}
onChange={()=>toggleIngredient(item)}
/>

{item}

</label>
))}

</div>

</div>

)

}