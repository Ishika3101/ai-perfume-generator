export default function PerfumeResult({result}){

if(!result) return null

return(

<div className="bg-white/20 backdrop-blur-xl rounded-2xl p-6 mt-6 text-center">

<h3 className="text-xl font-bold mb-3">
Generated Perfume
</h3>

<h2 className="text-2xl font-semibold mb-4">
{result.name}
</h2>

<p><b>Top Notes:</b> {result.top}</p>

<p><b>Heart Notes:</b> {result.heart}</p>

<p><b>Base Notes:</b> {result.base}</p>

</div>

)

}