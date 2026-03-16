export default function PerfumePyramid({ pyramid }) {

  if (!pyramid) return null

  return (

    <div className="bg-white/30 backdrop-blur-md p-8 rounded-xl shadow-md text-center">

      <h2 className="text-xl font-bold mb-6">
        Perfume Pyramid
      </h2>

      <div className="flex flex-col items-center space-y-6">

        {/* Top */}
        <div className="bg-white/40 px-6 py-2 rounded-lg w-40">
          <h3 className="font-semibold text-sm">Top Notes</h3>
          <p>{pyramid.top.join(", ") || "None"}</p>
        </div>

        {/* Heart */}
        <div className="bg-white/40 px-6 py-2 rounded-lg w-56">
          <h3 className="font-semibold text-sm">Heart Notes</h3>
          <p>{pyramid.heart.join(", ") || "None"}</p>
        </div>

        {/* Base */}
        <div className="bg-white/40 px-6 py-2 rounded-lg w-72">
          <h3 className="font-semibold text-sm">Base Notes</h3>
          <p>{pyramid.base.join(", ") || "None"}</p>
        </div>

      </div>

    </div>

  )
}