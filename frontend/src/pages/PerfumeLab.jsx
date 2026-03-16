import { useState } from "react"
import IngredientSelector from "../components/IngredientSelector"
import PerfumePyramid from "../components/PerfumePyramid"

export default function PerfumeLab() {

  const [selectedIngredients, setSelectedIngredients] = useState([])
  const [category, setCategory] = useState("")
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  const categories = [
    "sweet",
    "fresh",
    "woody",
    "luxury",
    "romantic",
    "masculine",
    "feminine"
  ]

  async function generatePerfume() {

    if (selectedIngredients.length === 0) {
      alert("Please select ingredients")
      return
    }

    if (!category) {
      alert("Please select fragrance profile")
      return
    }

    setLoading(true)

    try {

      const response = await fetch("https://ai-perfume-generator-3.onrender.com", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          ingredients: selectedIngredients,
          category: category
        })
      })

      const data = await response.json()

      setResult(data)

    } catch (error) {

      alert("Backend connection failed")

    }

    setLoading(false)
  }
  const categoryThemes = {
  sweet: "from-pink-400 to-rose-500",
  fresh: "from-blue-400 to-cyan-500",
  woody: "from-amber-600 to-yellow-700",
  luxury: "from-purple-600 to-indigo-700",
  romantic: "from-pink-500 to-purple-500",
  masculine: "from-slate-700 to-gray-900",
  feminine: "from-rose-400 to-pink-600"
} 
const activeTheme = categoryThemes[category] || "from-pink-400 to-pink-600"

  return (

    <div className={`min-h-screen bg-gradient-to-r ${activeTheme} p-10 transition-all duration-700`}>

      <h1 className="text-4xl font-bold text-center mb-10">
        AI Perfume Generator
      </h1>

      <div className="grid md:grid-cols-2 gap-8">

        {/* Ingredient Selector */}
        <div className="bg-white/30 backdrop-blur-md p-6 rounded-xl shadow-md">

          <h2 className="text-xl font-bold mb-4">
            Ingredient Lab
          </h2>

          <IngredientSelector
            onSelect={setSelectedIngredients}
          />

        </div>


        {/* Fragrance Profile */}
        <div className="bg-white/30 backdrop-blur-md p-6 rounded-xl shadow-md">

          <h2 className="text-xl font-bold mb-4">
            Fragrance Profile
          </h2>

          <div className="grid grid-cols-2 gap-4 mb-6">

            {categories.map((cat) => (

              <button
                key={cat}
                onClick={() => setCategory(cat)}
                className={`p-3 rounded-lg border 
                ${category === cat
                    ? "bg-white text-black"
                    : "border-white text-white"
                  }`}
              >
                {cat}
              </button>

            ))}

          </div>

          <button
            onClick={generatePerfume}
            className="w-full bg-black text-white py-3 rounded-xl hover:scale-[1.02] transition"
          >

            {loading
              ? "AI is crafting your perfume..."
              : "✨ Generate AI Fragrance"}

          </button>

        </div>

      </div>


      {/* RESULTS SECTION */}

      {result && (

        <div className="mt-12 space-y-10">

          {/* Formula + Chart */}
          <div className="grid md:grid-cols-2 gap-8">

            {/* Formula */}
            <div className="bg-white/30 backdrop-blur-md p-6 rounded-xl shadow-md">

              <h2 className="text-xl font-bold mb-4">
                Generated Formula
              </h2>

              <div className="space-y-2">

                {result.formula.map((item, i) => (

                  <p key={i}>
                    {item.ingredient} — {item.percentage.toFixed(2)}% | {item.ml.toFixed(2)} ml
                  </p>

                ))}

              </div>

            </div>


            {/* Chart */}
            <div className="bg-white/30 backdrop-blur-md p-6 rounded-xl shadow-md text-center">

              <h2 className="text-xl font-bold mb-4">
                Composition Chart
              </h2>

              {result.chart && (

                <img
                  src={`data:image/png;base64,${result.chart}`}
                  alt="chart"
                  className="mx-auto max-w-[260px]"
                />

              )}

            </div>

          </div>


          {/* Perfume Pyramid */}
          <div className="flex justify-center">

            <div className="w-[420px]">

              <PerfumePyramid pyramid={result.pyramid} />

            </div>

          </div>

        </div>

      )}

    </div>

  )
}