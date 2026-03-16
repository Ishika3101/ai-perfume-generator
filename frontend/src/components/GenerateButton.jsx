export default function GenerateButton({ onClick }) {

  return (

    <button
      onClick={onClick}
      className="w-full bg-black text-white py-4 rounded-xl hover:bg-gray-800 transition"
    >
      ✨ Generate AI Fragrance
    </button>

  )

}