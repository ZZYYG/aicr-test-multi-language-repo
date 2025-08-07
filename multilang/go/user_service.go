package user

import (
	"errors"
	"time"
)

// User 表示用户实体
type User struct {
	ID        string
	Username  string
	Email     string
	CreatedAt time.Time
	UpdatedAt time.Time
}

// UserService 用户服务
type UserService struct {
	repo UserRepository
}

// UserRepository 用户仓库接口
type UserRepository interface {
	FindByID(id string) (*User, error)
	Save(user *User) error
}

// NewUserService 创建用户服务
func NewUserService(repo UserRepository) *UserService {
	return &UserService{repo: repo}
}

// GetUser 获取用户
func (s *UserService) GetUser(id string) (*User, error) {
	if id == "" {
		return nil, errors.New("用户ID不能为空")
	}
	return s.repo.FindByID(id)
}

// CreateUser 创建用户
func (s *UserService) CreateUser(username, email string) (*User, error) {
	if username == "" {
		return nil, errors.New("用户名不能为空")
	}
	if email == "" {
		return nil, errors.New("邮箱不能为空")
	}
	
	now := time.Now()
	user := &User{
		ID:        generateID(),
		Username:  username,
		Email:     email,
		CreatedAt: now,
		UpdatedAt: now,
	}
	
	if err := s.repo.Save(user); err != nil {
		return nil, err
	}
	
	return user, nil
}

// generateID 生成唯一ID
func generateID() string {
	// 实际应用中应使用UUID等
	return "user_" + time.Now().Format("20060102150405")
}
