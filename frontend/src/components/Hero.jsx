import { Sparkles } from "lucide-react"

export default function Hero() {

return (

<div className="w-full min-h-[65vh] flex flex-col justify-center items-center text-center text-white px-6">

<Sparkles size={48} className="mb-6 opacity-80"/>

<h1 className="text-6xl font-bold mb-6">
AI Perfume Generator
</h1>

<p className="text-xl opacity-80 max-w-2xl">
Design unique fragrances using artificial intelligence. 
Select ingredients and fragrance styles to generate your 
own perfume composition.
</p>

</div>

)

}