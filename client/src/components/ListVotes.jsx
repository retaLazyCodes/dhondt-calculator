import VotesItem from './VotesItem';

function ListVotes({ 
  lists, 
  handleListsChange, 
  removeList,
}) {
  return (
    <div className="grid gap-2">
      {lists.map((list, i) => (
        <VotesItem
          key={i}
          list={list}
          index={i}
          handleListsChange={handleListsChange}
          removeList={removeList}
        />
      ))}
    </div>
  );
}

export default ListVotes;
