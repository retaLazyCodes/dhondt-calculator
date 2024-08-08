import React from 'react';

function SeatCountInput({ value, onChange }) {
  return (
    <div className="grid gap-2">
        <label htmlFor="seats" className="font-medium">
            Número de escaños
        </label>
        <input
            id="seats"
            type="number"
            min="1"
            max="100000"
            value={value}
            onChange={onChange}
            className="p-2 border rounded-md"
        />
    </div>
  );
}

export default SeatCountInput;
