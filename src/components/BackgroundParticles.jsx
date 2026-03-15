export default function BackgroundParticles(){

const particles = Array.from({ length: 30 })

return (

<div className="absolute inset-0 z-0 overflow-hidden pointer-events-none">

{particles.map((_,i)=>{

const size = Math.random()*8 + 4
const left = Math.random()*100
const duration = Math.random()*20 + 10

return (

<div
key={i}
className="absolute bg-white/40 rounded-full animate-ping"
style={{
width:`${size}px`,
height:`${size}px`,
left:`${left}%`,
top:`${Math.random()*100}%`,
animationDuration:`${duration}s`
}}
/>

)

})}

</div>

)

}