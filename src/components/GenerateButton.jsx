import { Sparkles } from "lucide-react"

export default function GenerateButton({onGenerate}) {

return (

<button
onClick={onGenerate}
className="w-full mt-6 p-4 bg-black text-white rounded-xl flex items-center justify-center gap-2 hover:scale-105 transition-all duration-200"
>

<Sparkles size={18}/>

Generate AI Fragrance

</button>

)

}