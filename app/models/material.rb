class Material < ApplicationRecord
  belongs_to :container
  has_many :items
end
