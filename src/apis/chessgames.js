CHESSGAMES_API= https://restapi.fr/api/chessgames

export async function deleteGame(_id){
    const response = await fetch(`${CHESSGAMES_API}/${_id}`, {
      method: 'DELETE',
    });
    if (response.ok) {
        return _id;
    } else {
      throw new Error("Error delete event");
    }
}

export async function getId(gameNumber) {
    try {
      const response = await fetch(`https://restapi.fr/api/chessgames?gameNumber=${gameNumber}`);
      if (response.ok) {
        const data = await response.json();
        // Supposons que data soit un tableau d'objets et que chaque objet a un attribut `id`
        // Retournez l'ID du premier élément correspondant trouvé, ou null s'il n'y a aucun élément correspondant
        return data.length > 0 ? data[0].id : null;
      } else {
        console.error('Failed to fetch data:', response.status);
        return null;
      }
    } catch (error) {
      console.error('Error while fetching data:', error);
      return null;
    }
  };