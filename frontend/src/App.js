import { useEffect, useState } from 'react'

import axios from 'axios'

import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  Polyline
} from 'react-leaflet'

import 'leaflet/dist/leaflet.css'

function App() {

  const [routeData, setRouteData] = useState(null)

  useEffect(() => {

    axios
      .get('http://127.0.0.1:5000/route')

      .then((response) => {

        setRouteData(response.data)

      })
      const interval = setInterval(() => {

  setRider((prev) => [

    prev[0] + (customer[0] - prev[0]) * 0.05,
prev[1] + (customer[1] - prev[1]) * 0.05

  ])

}, 1000)

return () => clearInterval(interval)

  }, [])

  const warehouse = [22.5726, 88.3639]

  const [rider, setRider] = useState([22.5760, 88.3680])

  const customer = [22.5826, 88.3739]

  const route = [
    warehouse,
    rider,
    customer
  ]

  return (

    <div>

      <h2 style={{
        textAlign: 'center'
      }}>

        Smart Delivery Tracking System

      </h2>

      {
        routeData && (

          <div style={{
            textAlign: 'center',
            marginBottom: '10px'
          }}>

            <h3>

              ETA:
              {routeData.delivery_eta}

            </h3>

            <h3>

              Rider:
              {routeData.assigned_rider}

            </h3>

          </div>
        )
      }

      <MapContainer
        center={warehouse}
        zoom={13}
        style={{
          height: "80vh",
          width: "100%"
        }}
      >

        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Marker position={warehouse}>
          <Popup>Warehouse</Popup>
        </Marker>

        <Marker position={rider}>
          <Popup>Delivery Rider</Popup>
        </Marker>

        <Marker position={customer}>
          <Popup>Customer</Popup>
        </Marker>

        <Polyline positions={route} />

      </MapContainer>

    </div>
  )
}

export default App