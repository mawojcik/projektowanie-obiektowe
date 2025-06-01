import Fluent
import Vapor

final class Product: Model, Content, @unchecked Sendable {
    static let schema = "products"
    
    @ID(key: .id)
    var id: UUID?

    @Field(key: "name")
    var name: String

    @Field(key: "description")
    var description: String

    @Field(key: "price")
    var price: Double

    required init() {}
    
    init(id: UUID? = nil, name: String, description: String, price: Double) {
        self.id = id
        self.name = name
        self.description = description
        self.price = price
    }
}


extension Product {
    struct Migration: AsyncMigration {
        func prepare(on database: any Database) async throws {
            try await database.schema(Product.schema)
                .id()
                .field("name", .string, .required)
                .field("description", .string, .required)
                .field("price", .double, .required)
                .create()
        }

        func revert(on database: any Database) async throws {
            try await database.schema(Product.schema).delete()
        }
    }
}
