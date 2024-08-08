import React from 'react';

function VotesItem({ 
  list, 
  index, 
  handleListsChange, 
  removeList, 
  disableVotesInput = false 
}) {
  return (
    <div className="flex gap-2">
      <input
        type="text"
        placeholder="List Name"
        value={list.name}
        onChange={(e) => handleListsChange(index, e.target.value, list.votes)}
        className="flex-1 p-2 border rounded-md"
        disabled={true}
      />
      <input
        type="number"
        min="0"
        value={list.votes}
        onChange={(e) => handleListsChange(index, list.name, e.target.value)}
        className="flex-1 p-2 border rounded-md"
        disabled={disableVotesInput}
      />
      <button
        onClick={() => removeList(index)}
        className="p-2 text-red-500 hover:bg-red-500/10 rounded-md"
      >
        🗑️
      </button>
    </div>
  );
}

export default VotesItem;
