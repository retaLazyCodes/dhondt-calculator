import React from 'react';

function VotesCountInput({ value, onChange }) {
  return (
    <div className="grid gap-2">
        <label htmlFor="votes" className="font-medium">
            Votos para la lista
        </label>
        <input
            id="votes"
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

export default VotesCountInput;
