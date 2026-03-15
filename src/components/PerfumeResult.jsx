import { FlaskConical } from "lucide-react"

export default function PerfumeResult({ result }){

if(!result) return null

return(

<div className="mt-6 bg-white/30 backdrop-blur-lg rounded-2xl p-6 text-white shadow-xl text-center">

{/* Perfume Bottle Icon */}

<div className="flex justify-center mb-4">
<FlaskConical size={40}/>
</div>

<h3 className="text-xl font-bold mb-4">
Generated Perfume
</h3>

<h2 className="text-2xl font-semibold mb-4">
{result.name}
</h2>

<div className="space-y-2 text-sm">

<p>
<strong>Top Notes:</strong> {result.top}
</p>

<p>
<strong>Heart Notes:</strong> {result.heart}
</p>

<p>
<strong>Base Notes:</strong> {result.base}
</p>

</div>

</div>

)

}   