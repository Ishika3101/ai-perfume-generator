import { useState } from "react"

const categories = [
"sweet",
"fresh",
"woody",
"luxury",
"romantic",
"masculine",
"feminine"
]

export default function FragranceCategory({ onSelect }){

const [selected,setSelected] = useState("")

function selectCategory(cat){
setSelected(cat)
onSelect(cat)
}

return(

<div>

<h2 className="text-2xl font-bold mb-4">
Fragrance Profile
</h2>

<div className="grid grid-cols-2 gap-4 mb-6">

{categories.map((cat)=>(
<button
key={cat}
onClick={()=>selectCategory(cat)}
className={`p-3 rounded-lg border ${
selected===cat ? "bg-white text-black" : ""
}`}
>

{cat}

</button>
))}

</div>

</div>

)

}