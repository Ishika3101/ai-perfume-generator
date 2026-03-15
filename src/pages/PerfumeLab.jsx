import IngredientSelector from "../components/IngredientSelector"
import FragranceCategory from "../components/FragranceCategory"
import GenerateButton from "../components/GenerateButton"
import PerfumeResult from "../components/PerfumeResult"
import BackgroundParticles from "../components/BackgroundParticles"
import Hero from "../components/Hero"
import { useState } from "react"

export default function PerfumeLab() {

const [result,setResult] = useState(null)
const [loading,setLoading] = useState(false)

function generatePerfume(){

setLoading(true)
setResult(null)

const perfumes = [

{
name:"Velvet Bloom",
top:"Citral, Limonene",
heart:"Geraniol, Nerol",
base:"Ambroxide, Musk"
},

{
name:"Golden Amber",
top:"Citral",
heart:"Phenylethyl Alcohol",
base:"Vanillin, Coumarin"
},

{
name:"Mystic Woods",
top:"Linalool",
heart:"Patchoulol",
base:"Vetiverol, Cashmeran"
}

]

setTimeout(()=>{

const random = perfumes[Math.floor(Math.random()*perfumes.length)]

setResult(random)
setLoading(false)

},3000)

}

return (

<div className="min-h-screen relative flex flex-col items-center bg-gradient-to-br from-purple-900 via-pink-700 to-orange-400">

{/* Background particles */}

<BackgroundParticles/>

{/* Hero section */}

<Hero/>

{/* Generator Section */}

<div className="grid grid-cols-2 gap-10 w-full max-w-6xl z-10 px-6 pb-20">

{/* LEFT PANEL */}

<IngredientSelector/>

{/* RIGHT PANEL */}

<div className="bg-white/20 backdrop-blur-xl rounded-2xl p-6 text-white shadow-xl">

<FragranceCategory/>

<GenerateButton onGenerate={generatePerfume}/>

{loading && (
<div className="mt-6 text-center text-white animate-pulse">
AI is crafting your perfume...
</div>
)}

{!loading && <PerfumeResult result={result}/>}

</div>

</div>

</div>

)

}