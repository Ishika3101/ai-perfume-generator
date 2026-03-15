import { useState } from "react"
import { categories } from "../data/ingredients"

export default function FragranceCategory(){

const [selected,setSelected] = useState("")

return(

<div>

<h2 className="text-2xl font-bold mb-4">
Fragrance Profile
</h2>

<p className="text-sm opacity-80 mb-4">
Choose the fragrance style you want.
</p>

<div className="grid grid-cols-2 gap-3">

{categories.map((cat)=>(

<button
key={cat}
onClick={()=>setSelected(cat)}
className={`p-3 rounded-xl border transition-all duration-200
${selected===cat
? "bg-white text-black"
: "bg-white/20 hover:bg-white/40"}
`}
>

{cat}

</button>

))}

</div>

</div>

)

}