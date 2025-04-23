import java.util.ArrayList;
import java.util.List;


public class Gedung2 {
    // --- Data Classes ---

    /**
     * Represents a single item within a room.
     */
    static class Item {
        private final String id;
        private final String type;

        public Item(String id, String type) {
            if (id == null || id.isBlank()) {
                throw new IllegalArgumentException("Item ID cannot be null or empty.");
            }
            if (type == null || type.isBlank()) {
                throw new IllegalArgumentException("Item type cannot be null or empty.");
            }
            this.id = id;
            this.type = type;
        }

        public String getId() {
            return id;
        }

        public String getType() {
            return type;
        }

        @Override
        public String toString() {
            // Provides a clear string representation of the item
            return type + " (ID: " + id + ")";
        }
    }

    /**
     * Represents a single room on a floor, containing items.
     */
    static class Room {
        private final int roomNumber; // Room number on its floor (e.g., 1, 2, 3...)
        private final List<Item> items;

        public Room(int roomNumber) {
            if (roomNumber <= 0) {
                throw new IllegalArgumentException("Room number must be positive.");
            }
            this.roomNumber = roomNumber;
            this.items = new ArrayList<>();
        }

        public void addItem(Item item) {
            if (item != null) {
                this.items.add(item);
            }
        }

        public int getRoomNumber() {
            return roomNumber;
        }

        public List<Item> getItems() {
            // Return an unmodifiable list or a copy if mutation from outside is a concern
            // For simplicity here, returning the direct list.
            return items;
        }

        @Override
        public String toString() {
            // Better representation than just the default list toString
            return "Room " + roomNumber + ": " + items;
        }
    }

    /**
     * Represents a single floor in a building, containing rooms.
     */
    static class Floor {
        private final int floorNumber; // Floor number in the building (e.g., 1, 2, 3...)
        private final List<Room> rooms;

        public Floor(int floorNumber) {
            if (floorNumber <= 0) {
                throw new IllegalArgumentException("Floor number must be positive.");
            }
            this.floorNumber = floorNumber;
            this.rooms = new ArrayList<>();
        }

        public void addRoom(Room room) {
            if (room != null) {
                this.rooms.add(room);
            }
        }

        public int getFloorNumber() {
            return floorNumber;
        }

        public List<Room> getRooms() {
            return rooms;
        }

        @Override
        public String toString() {
            return "Floor " + floorNumber; // Rooms will be printed separately for clarity
        }
    }

    /**
     * Represents the entire building, containing floors.
     */
    static class Building {
        private final String buildingId;
        private final List<Floor> floors;

        // --- Constants ---
        private static final String DEFAULT_BUILDING_ID_PREFIX = "GdgA"; // Example: Gedung A
        private static final String[] DEFAULT_ITEM_TYPES = {"Lamp", "Cabinet", "Fan", "Switch"};

        public Building(String buildingId) {
            if (buildingId == null || buildingId.isBlank()) {
                throw new IllegalArgumentException("Building ID cannot be null or empty.");
            }
            this.buildingId = buildingId;
            this.floors = new ArrayList<>();
        }

        public void addFloor(Floor floor) {
            if (floor != null) {
                this.floors.add(floor);
            }
        }

        public String getBuildingId() {
            return buildingId;
        }

        public List<Floor> getFloors() {
            return floors;
        }

        /**
         * Populates the building with a specified number of floors and rooms per floor,
         * adding default items to each room.
         *
         * @param numberOfFloors The total number of floors to create.
         * @param roomsPerFloor  The number of rooms to create on each floor.
         */
        public void populateBuilding(int numberOfFloors, int roomsPerFloor) {
            if (numberOfFloors <= 0 || roomsPerFloor <= 0) {
                System.err.println("Warning: Number of floors and rooms per floor must be positive. Building not populated.");
                return;
            }

            this.floors.clear(); // Clear existing floors if any

            for (int i = 0; i < numberOfFloors; i++) {
                int currentFloorNumber = i + 1; // User-facing floor number (starts from 1)
                Floor floor = new Floor(currentFloorNumber);

                for (int j = 0; j < roomsPerFloor; j++) {
                    int currentRoomNumber = j + 1; // User-facing room number (starts from 1)
                    Room room = new Room(currentRoomNumber);

                    // Add default items to this room
                    for (String itemType : DEFAULT_ITEM_TYPES) {
                        // Generate a unique ID for each item
                        String itemId = String.format("%s-F%d-R%d-%s",
                                this.buildingId,
                                currentFloorNumber,
                                currentRoomNumber,
                                itemType.toUpperCase().substring(0, Math.min(3, itemType.length())) // e.g., LAM, CAB
                        );
                        // Optional: Add a sequence number if multiple items of the same type exist per room
                        // String itemId = String.format("%s-F%d-R%d-%s-%03d", ... buildingId, floor, room, type, itemIndex);

                        Item item = new Item(itemId, itemType);
                        room.addItem(item);
                    }
                    floor.addRoom(room);
                }
                this.addFloor(floor);
            }
        }

        /**
         * Prints the inventory of the entire building to the console.
         */
        public void displayInventory() {
            System.out.println("==========================================");
            System.out.println("Inventory for Building: " + this.buildingId);
            System.out.println("==========================================");

            if (this.floors.isEmpty()) {
                System.out.println("Building is empty.");
                return;
            }

            for (Floor floor : this.floors) {
                System.out.println("\n--- " + floor + " ---"); // Uses Floor's toString()
                if (floor.getRooms().isEmpty()) {
                    System.out.println("  No rooms on this floor.");
                } else {
                    for (Room room : floor.getRooms()) {
                        // Using Room's toString() which includes items
                        System.out.println("  " + room);
                    }
                }
            }
            System.out.println("\n==========================================");
        }


        
    }
    // --- Main Application Logic ---

    public static void main(String[] args) {
        // Configuration
        final int numberOfFloors = 2;
        final int roomsPerFloor = 5;
        final String buildingName = "GdgA";

        // 1. Create the Building
        Building buildingA = new Building(buildingName);

        // 2. Populate the Building with Floors, Rooms, and Items
        buildingA.populateBuilding(numberOfFloors, roomsPerFloor);

        // 3. Display the Inventory
        buildingA.displayInventory();

        // --- Example: Accessing specific data (Optional) ---
        System.out.println("\n--- Example Access ---");
        if (!buildingA.getFloors().isEmpty() && !buildingA.getFloors().get(0).getRooms().isEmpty()) {
            Floor firstFloor = buildingA.getFloors().get(0); // Floor 1 (index 0)
            Room firstRoomOnFirstFloor = firstFloor.getRooms().get(0); // Room 1 (index 0)

            System.out.println("Items in " + firstFloor + ", " + "Room " + firstRoomOnFirstFloor.getRoomNumber() + ":");
            if (!firstRoomOnFirstFloor.getItems().isEmpty()) {
                Item firstItem = firstRoomOnFirstFloor.getItems().get(0);
                System.out.println(" - First item type: " + firstItem.getType());
                System.out.println(" - First item ID:   " + firstItem.getId());
            } else {
                System.out.println(" - No items in this room.");
            }
        } else {
            System.out.println("Building structure not available for example access.");
        }
    }
}
